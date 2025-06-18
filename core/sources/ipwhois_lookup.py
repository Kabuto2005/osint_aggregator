# osint_aggregator/core/sources/ipwhois_lookup.py
from ipwhois import IPWhois

def get_whois(ip):
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        return {
            "Network Name": results.get("network", {}).get("name", "N/A"),
            "Org Name": results.get("network", {}).get("org", {}).get("name", "N/A"),
            "CIDR": results.get("network", {}).get("cidr", "N/A"),
            "ASN": results.get("asn", "N/A"),
            "Country": results.get("asn_country_code", "N/A")
        }
    except Exception as e:
        return {"Error": str(e)}
