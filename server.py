import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()

print(f"Server is listening on port 5000...")
while True:
    conn, addr = server.accept()
    conn.close()
    
