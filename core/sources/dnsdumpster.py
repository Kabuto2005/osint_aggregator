# osint_aggregator/core/sources/dnsdumpster.py
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://dnsdumpster.com/"

def get_dns_info(domain):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114 Safari/537.36"
    }

    try:
        # Get CSRF token
        res = session.get(BASE_URL, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        csrf = soup.find("input", {"name": "csrfmiddlewaretoken"}).get("value")
        cookies = res.cookies.get_dict()

        # Submit domain with token
        data = {
            "csrfmiddlewaretoken": csrf,
            "targetip": domain
        }
        res = session.post(BASE_URL, headers=headers, cookies=cookies, data=data)
        soup = BeautifulSoup(res.text, "html.parser")

        results = []
        tables = soup.find_all("table")
        if not tables:
            return ["[!] No data found or blocked by DNSDumpster."]

        # Parse DNS records from tables
        for table in tables:
            for row in table.find_all("tr")[1:]:  # Skip header row
                cols = row.find_all("td")
                if len(cols) >= 1:
                    entry = " | ".join(col.text.strip() for col in cols if col.text.strip())
                    results.append(entry)

        return results if results else ["[!] No structured DNS data found."]
    except Exception as e:
        return [f"[!] DNSDumpster error: {e}"]
