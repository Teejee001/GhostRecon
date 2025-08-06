# 👻 GhostRecon

**GhostRecon** is an advanced OSINT and bug bounty reconnaissance tool designed for gathering vital intelligence on domains and websites. It performs WHOIS lookups, IP information gathering, subdomain enumeration, email extraction, and exposure checks.

> 🔒 **For educational and ethical hacking purposes only. Do not use on unauthorized targets.**

---

## ✨ Features

- 🔍 WHOIS Lookup
- 🌐 IP Geolocation and Network Info
- 🕵️ Subdomain Enumeration (via crt.sh)
- 📧 Email Extraction from Target Website
- ⚔️ Domain Exposure Detection
- 📄 PDF Report Generation
- 🐙 Bug Bounty Recon Utility

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt

Dependencies include:

requests

reportlab

beautifulsoup4

whois


💻 Usage
Basic syntax:

bash
python3 main.py --url <target_domain> [options]


🔧 Examples

WHOIS lookup:

python3 main.py --url example.com --whois

Subdomain enumeration:

python3 main.py --url example.com --subdomains

Extract emails from website:

python3 main.py --url https://example.com --emails

All-in-one:

python3 main.py --url example.com --whois --ipinfo --subdomains --emails --check-stealer --save results

📁 Output
Results are saved in the results/ directory

Each scan is stored as a .txt and .pdf report

⚠️ Disclaimer
This tool is developed strictly for educational and authorized security testing. The author is not responsible for any misuse or illegal activity carried out using this tool.

🛡 License
This project is licensed under the MIT License.

👨‍💻 Developer
Created with ❤️ by Teejay001/Ghostynox

GitHub: Teejay001
