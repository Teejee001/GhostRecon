import re
import requests
from bs4 import BeautifulSoup

def extract_emails_from_url(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url  # Add scheme if missing

        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", soup.get_text()))
        return list(emails)

    except Exception as e:
        return {"error": str(e)}
