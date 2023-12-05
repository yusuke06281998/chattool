import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 50007))

client_socket.sendall(b'Hellow world')
data = client_socket.recv(1024)
print('Received from server_socket:', repr(data))

client_socket.close()