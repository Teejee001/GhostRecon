import subprocess

def run_amass(domain):
    try:
        result = subprocess.run(
            ["amass", "enum", "-d", domain, "-silent"],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            return {"error": result.stderr.strip()}
        
        subdomains = result.stdout.strip().split("\n")
        return [sub.strip() for sub in subdomains if sub.strip()]
    except Exception as e:
        return {"error": str(e)}
