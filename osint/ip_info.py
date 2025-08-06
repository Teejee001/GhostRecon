import requests
import socket

def ip_info(domain):
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        data = response.json()
        data['ip'] = ip
        return data
    except Exception as e:
        return {"error": str(e)}
