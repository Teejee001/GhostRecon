# GhostRecon 🕵️‍♂️

GhostRecon is an advanced Bug Bounty & OSINT Reconnaissance tool built with Python. It is designed to automate reconnaissance tasks during penetration testing or bug bounty engagements.

## 💡 Features

- 🔍 Subdomain Enumeration (via Amass + crt.sh)
- 📧 Email Address Extraction
- 🌐 WHOIS Lookup
- 🛰️ IP Info Lookup
- 🛡️ Domain Exposure Check (Leak Detection)
- 📝 Generates PDF Reports
- 📁 Saves structured results in folders
- 💻 CLI-based usage, lightweight, and fast

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/GhostRecon.git
cd GhostRecon
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Usage Examples

Here are some common commands you can use with GhostRecon:

```bash
# Perform WHOIS lookup
python3 main.py --url example.com --whois

# Get IP info
python3 main.py --url example.com --ipinfo

# Enumerate subdomains (using crt.sh and Amass)
python3 main.py --url example.com --subdomains

# Extract emails from the target domain
python3 main.py --url https://example.com --emails

# Check for domain exposure on known breaches
python3 main.py --url example.com --check-stealer

# Save results as text and PDF
python3 main.py --url example.com --whois --ipinfo --save results

📂 Output
All results are printed to the terminal

Reports are saved in the results/ folder

PDF files are automatically generated if --save is used


📄 License
This project is licensed under the MIT License — you are free to use, modify, and share.


🤝 Contributing
Feel free to fork the repo, improve the tool, and submit pull requests.


👨‍💻 Developer
Built by Ghostynox 🐱‍💻 for the cybersecurity community.



⚠️ Disclaimer
This tool is developed strictly for educational and ethical penetration testing purposes only.
Unauthorized scanning or reconnaissance on websites without proper authorization is illegal and against GitHub's Terms of Service.
The developers are not responsible for any misuse of this tool.
