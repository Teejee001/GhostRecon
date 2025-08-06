import whois

def whois_lookup(domain):
    try:
        data = whois.whois(domain)
        result = {
            "domain": data.domain_name if hasattr(data, 'domain_name') else None,
            "registrar": data.registrar if hasattr(data, 'registrar') else None,
            "created": str(data.creation_date) if hasattr(data, 'creation_date') else None,
            "expires": str(data.expiration_date) if hasattr(data, 'expiration_date') else None,
            "emails": data.emails if hasattr(data, 'emails') else None
        }
        return result
    except Exception as e:
        return {"error": str(e)}
