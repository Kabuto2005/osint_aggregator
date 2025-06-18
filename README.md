🕵️ OSINT Aggregator CLI

A lightweight, modular Python tool to collect open-source intelligence (OSINT) from public sources without requiring API keys. It supports IP, domain, and email-based scans with output saved to a formatted file.



🚀 Features
	•	Subdomain enumeration via crt.sh
	•	Passive DNS and infrastructure lookups via dnsdumpster.com
	•	IP ownership and ASN info via RDAP (ipwhois)
	•	Output saved to output_<target>.txt
	•	CLI interface (GUI coming soon)


📦 Requirements

Install Python dependencies:

pip install -r requirements.txt


⚙️ Usage

Run from the command line:

python3 cli.py --domain example.com --ip 1.2.3.4

Optional Flags
	•	--domain – Target domain (for crt.sh + DNSDumpster)
	•	--ip – IP address (for WHOIS)
	•	--email – (Stubbed, for future HIBP integration)
	•	--username – (For future modules)

Example:

python3 cli.py --domain github.com --ip 140.82.113.3


📁 Output

The tool generates a file like:
output_github_com_140_82_113_3.txt

Containing:
	•	Subdomains
	•	DNS infrastructure
	•	WHOIS metadata


🛠 Roadmap
	•	Add HIBP (HaveIBeenPwned) API integration
	•	Add Google/Bing dorking
	•	Add full GUI with search history
	•	Export results as JSON/CSV


⚠️ Legal

Use responsibly. This tool is for educational and authorized auditing purposes only. Unauthorized scanning or data collection may be illegal.


Author:
David Osisek
MIT IT Security, BS Software Dev and Analysis
