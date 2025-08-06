import requests
import json
import os

def enumerate_subdomains(domain):
    cache_file = f"cache/{domain.replace('.', '_')}_subdomains.json"

    try:
        # Make the HTTPS request to crt.sh
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        res = requests.get(url, timeout=10)
        entries = res.json()

        # Use a set to avoid duplicates
        subs = set()
        for e in entries:
            for s in e['name_value'].split('\n'):
                if domain in s:
                    subs.add(s.strip())

        subdomains = sorted(subs)

        # Save to cache
        os.makedirs("cache", exist_ok=True)
        with open(cache_file, "w") as f:
            json.dump(subdomains, f, indent=2)

        return subdomains

    except Exception as e:
        # Fallback to cached results if available
        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                return json.load(f)
        return {"error": str(e)}
