import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        result = {
            "domain": domain,
            "registrar": w.registrar,
            "created": str(w.creation_date),
            "expires": str(w.expiration_date),
            "emails": w.emails,
        }
        return result
    except Exception as e:
        return {"error": str(e)}
