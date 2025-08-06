import requests
import re

def scrape_website(url, find_emails=False, find_phones=False, find_links=False):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        html = response.text
        results = {}

        if find_emails:
            emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
            results["emails"] = list(set(emails))

        if find_phones:
            phones = re.findall(r"\+?\d[\d -]{8,}\d", html)
            results["phones"] = list(set(phones))

        if find_links:
            links = re.findall(r'href=["\'](http[s]?://[^"\']+)["\']', html)
            results["links"] = list(set(links))

        return results

    except Exception as e:
        return {"error": str(e)}
