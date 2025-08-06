import argparse
import json
import sys
import time
import threading
from datetime import datetime

from core.banner import display_banner, Colors
from core.connection import check_connection
from core.validation import is_valid_url
from core.scraper import scrape_website
from core.save import save_results

from osint.whois_lookup import whois_lookup
from osint.ip_info import ip_info
from osint.subdomain_enum import enumerate_subdomains
from osint.amass_enum import run_amass
from osint.email_extract import extract_emails_from_url
from osint.cavalier_check import check_domain_exposure

# Animation loader
def loading_animation(stop_event, message):
    animation = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{Colors.BrightCyan}{animation[idx % len(animation)]} {message}{Colors.Reset}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")

def start_loading(message):
    stop_event = threading.Event()
    thread = threading.Thread(target=loading_animation, args=(stop_event, message))
    thread.daemon = True
    thread.start()
    return stop_event

def format_section(title, content, color="\033[1;97m"):
    if not content:
        return f"{color}[{title}]\033[0m\nNo data available"
    if isinstance(content, dict):
        formatted = []
        for k, v in content.items():
            if isinstance(v, list):
                v = "\n    ".join(v)
            formatted.append(f"{k}: {v}")
        content = "\n".join(formatted)
    elif isinstance(content, list):
        content = "\n".join(f"  • {item}" for item in content)
    return f"{color}[{title}]\033[0m\n{content}"

def main():
    parser = argparse.ArgumentParser(description="GhostRecon - Bug Bounty/OSINT Tool")
    parser.add_argument("--url", required=True)
    parser.add_argument("--whois", action="store_true")
    parser.add_argument("--ipinfo", action="store_true")
    parser.add_argument("--subdomains", action="store_true")
    parser.add_argument("--emails", action="store_true")
    parser.add_argument("--check-stealer", action="store_true")
    parser.add_argument("--save", type=str, help="Folder to save results")
    args = parser.parse_args()

    display_banner()
    check_connection()

    if not is_valid_url(args.url):
        print("\033[1;91m[ERROR] Invalid URL.\033[0m")
        return

    domain = args.url.split("//")[-1].split("/")[0]
    print(f"\n{Colors.BrightCyan}[*] Scanning: {domain}{Colors.Reset}\n")

    results = {}

    if args.emails:
        stop_event = start_loading("Extracting emails...")
        results['emails'] = extract_emails_from_url(args.url)
        stop_event.set()
        time.sleep(0.1)

    if args.whois:
        stop_event = start_loading("Performing WHOIS lookup...")
        results['whois'] = whois_lookup(domain)
        stop_event.set()
        time.sleep(0.1)

    if args.ipinfo:
        stop_event = start_loading("Getting IP info...")
        results['ipinfo'] = ip_info(domain)
        stop_event.set()
        time.sleep(0.1)

    if args.subdomains:
        stop_event = start_loading("Enumerating subdomains...")
        results['subdomains'] = enumerate_subdomains(domain)
        stop_event.set()
        time.sleep(0.1)

    if args.check_stealer:
        stop_event = start_loading("Checking domain exposure...")
        results['cavalier'] = check_domain_exposure(domain)
        stop_event.set()
        time.sleep(0.1)

    print(f"\n{Colors.BrightGreen}[+] Scan completed!{Colors.Reset}\n")
    print(f"{Colors.BrightGreen}" + "─" * 80 + Colors.Reset)

    colors = {
        'WHOIS': '\033[1;92m',
        'IPINFO': '\033[1;94m',
        'SUBDOMAINS': '\033[1;95m',
        'EMAILS': '\033[1;96m',
        'CAVALIER': '\033[1;93m',
        'ERROR': '\033[1;91m',
    }

    for k, v in results.items():
        color = colors.get(k.upper(), '\033[1;97m')
        print(format_section(k.upper(), v, color))
        print("\n" + "─" * 80 + "\n")

    if args.save:
        stop_event = start_loading("Saving results...")
        save_results(results, args.save, domain)
        stop_event.set()
        time.sleep(0.1)
        print(f"\n{Colors.BrightGreen}[+] PDF report generated: {args.save}/{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf{Colors.Reset}")

if __name__ == "__main__":
    main()
