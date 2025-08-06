import requests

def check_domain_exposure(domain):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breaches"
        headers = {
            "User-Agent": "GhostRecon",
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return {"error": f"API response: {response.status_code}"}
        
        breaches = response.json()
        exposed_sites = []

        for breach in breaches:
            if domain.lower() in breach.get("Domain", "").lower():
                exposed_sites.append({
                    "Name": breach["Name"],
                    "BreachDate": breach["BreachDate"],
                    "Description": breach["Description"]
                })

        return exposed_sites if exposed_sites else ["No known breaches found for domain"]

    except Exception as e:
        return {"error": str(e)}
