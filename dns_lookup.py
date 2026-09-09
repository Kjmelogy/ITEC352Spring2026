import socket

website = input("Enter a website URL (e.g., www.example.com): ")

try:
    result = socket.gethostbyname_ex(website)
    ip_addresses = result[2]
    print(f"IP addresses for {website}")
    for ip in ip_addresses:
        print(ip)

except socket.gaierror:
    print(f"Error: Unable to resolve the hostname {website}")
