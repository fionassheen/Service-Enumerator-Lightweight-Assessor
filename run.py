import argparse, json
from scanner import run_scan
from banner import grab_banner
from assessor import assess_port
from reporter.make_report import make_report

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--target', required=True, help='target IP or hostname')
    p.add_argument('--ports', default='1-1024', help='port range for nmap (e.g. 1-1024)')
    p.add_argument('--out', default='report.html', help='output HTML file')
    args = p.parse_args()

    # 1. Run nmap scan
    print(f'[+] Running nmap scan on {args.target} ports {args.ports} ...')
    scan = run_scan(args.target, args.ports)

    # 2. Grab banners and assess each open port
    enriched = []
    for pinfo in scan.get('open_ports', []):
        port = pinfo.get('port')
        print(f'    - port {port} ({pinfo.get("service")}) ... grabbing banner')
        banner_text = grab_banner(args.target, port)
        pinfo['host'] = args.target
        assessed = assess_port(pinfo, banner_text)
        enriched.append(assessed)

    # 3. Prepare final data dict
    final = {'target': scan.get('target'), 'open_ports': enriched}

    # 4. Save JSON for debugging (optional)
    with open('scan_results.json', 'w') as f:
        json.dump(final, f, indent=2)

    # 5. Make report
    print('[+] Generating report...')
    make_report(final, out_html=args.out)
    print(f'[+] Report written to {args.out}')

if __name__ == '__main__':
    main()
