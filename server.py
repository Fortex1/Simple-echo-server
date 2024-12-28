import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:  
        print('Connection closed by client')
        break
    print(f"Received: {data}")
    conn.send(data.upper().encode('utf-8'))  

conn.close()