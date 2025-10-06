import ftplib

def check_ftp_anonymous(host):
    """Check if anonymous FTP login is allowed."""
    try:
        ftp = ftplib.FTP(host, timeout=3)
        ftp.login('anonymous', 'anonymous@domain.com')
        ftp.quit()
        return True
    except Exception:
        return False

def assess_port(port_info, banner_text=''):
    """
    port_info: dict with keys 'port', 'service', 'product', 'version'
    banner_text: banner string (may be empty)
    returns: dict with added severity and note
    """
    svc = (port_info.get('service') or '').lower()
    product = (port_info.get('product') or '').lower()
    version = (port_info.get('version') or '').lower()

    severity = 'low'
    note = ''

    if svc == 'ftp':
        severity = 'high'
        note = 'FTP detected — checking for anonymous login...'
        # Try anonymous login check
        host = port_info.get('host', '127.0.0.1')  # fallback
        if check_ftp_anonymous(host):
            severity = 'critical'
            note += ' Anonymous FTP login allowed!'
        else:
            note += ' Anonymous login disabled.'
    elif svc == 'telnet':
        severity = 'high'
        note = 'Telnet is insecure (cleartext). Recommend disabling and using SSH.'
    elif 'ssh' in svc:
        severity = 'medium'
        note = 'SSH present — verify allowed ciphers and user permissions.'
    elif 'http' in svc or port_info.get('port') in (80, 8080, 8000):
        if 'apache' in product or 'nginx' in product:
            severity = 'medium'
            note = 'HTTP server detected — check for directory listing and outdated server.'
    else:
        severity = 'low'

    # If banner mentions "anonymous" (e.g., FTP), raise severity
    if 'anonymous' in (banner_text or '').lower():
        severity = 'critical'
        note = (note + ' Anonymous access detected in banner.').strip()

    result = dict(port_info)
    result.update({'severity': severity, 'note': note, 'banner': banner_text})
    return result

