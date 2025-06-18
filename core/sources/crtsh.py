# osint_aggregator/core/sources/crtsh.py
import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return ["[!] crt.sh returned non-200 status."]

        data = res.json()
        subdomains = set()
        for entry in data:
            name = entry.get("name_value")
            if name:
                for line in name.split("\n"):
                    if domain in line:
                        subdomains.add(line.strip())

        return sorted(subdomains)
    except Exception as e:
        return [f"[!] Error querying crt.sh: {e}"]
