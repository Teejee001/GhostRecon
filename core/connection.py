import requests
from core.banner import Colors

def check_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        print(f"{Colors.BrightGreen}[*] Connected.{Colors.Reset}")
    except requests.ConnectionError:
        print(f"{Colors.BrightRed}[ERROR] No internet connection.{Colors.Reset}")
        exit(1)
