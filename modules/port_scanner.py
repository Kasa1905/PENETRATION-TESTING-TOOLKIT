class PortScanner:
    def __init__(self):
        pass

    def scan_ports(self, target):
        import socket
        open_ports = []
        for port in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports

    def display_results(self, results):
        if results:
            print(f"Open ports: {', '.join(map(str, results))}")
        else:
            print("No open ports found.")