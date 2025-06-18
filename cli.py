# osint_aggregator/cli.py
import argparse
from core.query_dispatcher import run_osint_scan

def main():
    parser = argparse.ArgumentParser(description="OSINT Aggregator CLI")
    parser.add_argument("--email", help="Email address to scan")
    parser.add_argument("--ip", help="IP address to scan")
    parser.add_argument("--username", help="Username to scan")
    parser.add_argument("--domain", help="Domain name to scan")
    args = parser.parse_args()

    targets = {
        "email": args.email,
        "ip": args.ip,
        "username": args.username,
        "domain": args.domain
    }

    # Build dynamic output filename
    identifier = "_".join(filter(None, [args.email, args.ip, args.username, args.domain]))
    safe_name = identifier.replace("@", "_at_").replace(".", "_")
    output_file = f"output_{safe_name}.txt"

    print(f"\n[+] Output will be saved to: {output_file}\n")
    run_osint_scan(targets, output_file)

if __name__ == "__main__":
    main()
