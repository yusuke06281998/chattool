import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 50007))

input_text = input(">")
s.send(input_text.encode('utf-8'))
# s.sendall(b'hello world')

data = s.recv(1024)
print(repr(data))

s.close()
