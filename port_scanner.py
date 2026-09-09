import socket

target = input(f"Enter an IP address or hostname: ")

for port in range(1, 101):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = scanner.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")
