# osint_aggregator/core/query_dispatcher.py
from core.sources import crtsh, ipwhois_lookup, dnsdumpster

def run_osint_scan(targets, output_file):
    results = []

    # crt.sh & DNSDumpster
    if targets.get("domain"):
        results.append("[crt.sh] Subdomain Certificate Search:")
        subdomains = crtsh.get_subdomains(targets["domain"])
        results.extend([f" - {sd}" for sd in subdomains])

        results.append("\n[DNSDumpster] Passive DNS and Subdomain Info:")
        dns_info = dnsdumpster.get_dns_info(targets["domain"])
        results.extend([f" - {entry}" for entry in dns_info])

    # IP RDAP Lookup
    if targets.get("ip"):
        results.append("\n[IPWhois] IP Ownership Lookup:")
        whois_info = ipwhois_lookup.get_whois(targets["ip"])
        results.extend([f"{k}: {v}" for k, v in whois_info.items()])

    # Write to file
    with open(output_file, "w") as f:
        for line in results:
            f.write(line + "\n")

    print("[+] OSINT scan complete.")
    print("[+] Results written to:", output_file)
