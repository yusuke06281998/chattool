import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 50007))
s.listen(1)
client_obj, client_address = s.accept()

print(client_address)

data = client_obj.recv(1024)
client_obj.sendall(data)

client_obj.close()
s.close()