import socket

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 50007))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

while True:
    data = client_socket.recv(1024)
    if not data:break
    print('Received', repr(data))
    client_socket.sendall(data)

client_socket.close()