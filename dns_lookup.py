import socket
from concurrent.futures import ThreadPoolExecutor

target = input(f"Enter an IP address or hostname: ")
target = socket.gethostbyname(target)

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        scanner.settimeout(0.05)
        result = scanner.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
            print(f"Port {port} is OPEN - Service: {service}")
        except OSError:
            print(f"Port {port} is OPEN - Service: Unknown")

with ThreadPoolExecutor(max_workers=200) as executor:
    executor.map(scan_port, range(1, 5001))
print(f"Port scanning completed for {target}.") 
