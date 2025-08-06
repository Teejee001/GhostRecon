import requests
import time

def enumerate_subdomains(domain, retries=2, timeout=30):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    
    for attempt in range(retries + 1):
        try:
            res = requests.get(url, timeout=timeout)
            entries = res.json()

            subs = set()
            for e in entries:
                for s in e['name_value'].split('\n'):
                    if domain in s:
                        subs.add(s.strip())
            return list(sorted(subs))

        except requests.exceptions.Timeout:
            if attempt < retries:
                time.sleep(3)  # wait before retry
                continue
            return {"error": f"Timeout after {retries + 1} attempts (timeout={timeout}s)"}
        
        except Exception as e:
            return {"error": str(e)}
