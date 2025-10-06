import nmap
import json

def run_scan(target, ports='1-1024'):
    nm = nmap.PortScanner()
    # -sV to detect service/version
    nm.scan(hosts=target, ports=ports, arguments='-sV --open')
    results = {'target': target, 'open_ports': []}
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in sorted(nm[host][proto].keys()):
                svc = nm[host][proto][port]
                results['open_ports'].append({
                    'port': port,
                    'protocol': proto,
                    'state': svc.get('state'),
                    'service': svc.get('name'),
                    'product': svc.get('product', ''),
                    'version': svc.get('version', ''),
                })
    return results

if __name__ == '__main__':
    import sys
    tgt = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    ports = sys.argv[2] if len(sys.argv) > 2 else '1-1024'
    print(json.dumps(run_scan(tgt, ports), indent=2))
