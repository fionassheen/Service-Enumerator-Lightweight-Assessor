Service Enumerator & Lightweight Assessor

Overview:
This project is a Python-based network reconnaissance and assessment tool developed as part of my cybersecurity internship.  
It scans a target for open ports and running services, captures banners, performs lightweight analysis for misconfigurations, and generates a clear, formatted HTML report.
The goal of this tool is to automate basic enumeration and provide quick insights into potential security risks — all in an ethical, controlled lab environment.

Objective:
- To perform port enumeration and service detection on target systems.  
- To identify service banners and version information.  
- To apply simple rule-based vulnerability checks (e.g., FTP anonymous login).  
- To generate a structured and professional HTML report summarizing findings.  

Tools and Technologies Used:
Python 3 - Core programming language 
Nmap/python-nmap - Port and service detection
Socket - Banner grabbing 
ftplib - FTP anonymous login test 
Jinja2 - HTML report generation 
Rich - Console output formatting 
Kali Linux - Testing and execution environment 

Implementation:

1. Port Scanning
Uses `python-nmap` with service version detection (`-sV`) to enumerate open ports and identify active services.

2. Banner Grabbing
Attempts to retrieve initial response data from services (e.g., `OpenSSH`, `Apache`) for version identification.

3. Assessment Rules
Simple checks are applied for potential issues, such as:
- Insecure services (FTP, Telnet)
- Anonymous FTP login detection
- Outdated or misconfigured web servers

4. Reporting
All results are compiled into:
- `scan_results.json` – structured machine-readable data  
- `report.html` – user-friendly formatted report 

How to Run:

Step 1: Setup
# Clone repository
git clone https://github.com/<your-username>/service-enumerator.git
cd service-enumerator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install python-nmap jinja2 rich

Step 2: Run Scan
python3 run.py --target <TARGET_IP> --ports 1-1024 --out report.html

Example:
python3 run.py --target 127.0.0.1 --ports 21,22,80 --out report.html

Step 3: View Results
Open the generated report.html file in any web browser to view:
 1. Target details
 2. Open ports
 3. Detected services
 4. Severity ratings and notes

Example Output
Sample Table View:
Port	Service	Product/Version	Severity	Note
21	FTP	vsftpd 3.0.3	 Critical	Anonymous FTP login allowed
22	SSH	OpenSSH 8.9	 Medium	SSH detected – verify allowed ciphers
80	HTTP	Apache 2.4.52	 Low	HTTP server detected – up to date

Generated Files:
 scan_results.json
 report.html

File Structure
raf_port_enumerator/
│
├── scanner.py          # Nmap-based port and service scanner
├── banner.py           # Banner grabber
├── assessor.py         # Rules and checks (FTP, Telnet, HTTP, etc.)
├── reporter/
│   ├── make_report.py  # HTML report generator
│   └── templates/
│       └── report.html # HTML template for report
├── run.py              # Main executable script
├── scan_results.json   # Output data (sample)
├── report.html         # Generated HTML report
└── README.md           # Documentation

Author
Name: Fiona S Sheen
Environment: Kali Linux (VMware)

Ethical Use Notice
This tool is built strictly for educational and authorized penetration testing purposes.
Unauthorized scanning, probing, or exploitation of systems without consent is ILLEGAL AND UNETHICAL.
Use only on systems you OWN OR HAVE EXPLICIT written permission to test.
