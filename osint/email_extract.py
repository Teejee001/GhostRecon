import requests
import re

def extract_emails_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        html = response.text
        # Simple regex for email matching
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html)
        return sorted(set(emails)) if emails else ["No emails found"]
    except Exception as e:
        return {"error": str(e)}
