import socket

def grab_banner(host, port, timeout=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    banner = ''
    try:
        s.connect((host, int(port)))
        # send tiny probe for HTTP (optional)
        if port in (80, 8080, 8000):
            s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        else:
            try:
                s.send(b'\r\n')
            except:
                pass
        data = s.recv(1024)
        banner = data.decode('utf-8', errors='ignore').strip()
    except Exception:
        banner = ''
    finally:
        try:
            s.close()
        except:
            pass
    return banner
