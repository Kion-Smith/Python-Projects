import socket

host = "localhost"
port = 65432
#having problems getting this to work
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
connection , address = s.accept()
print("Connected", address)
