import socket

# The first input of the socket of the is AF INTET which is a ipv4 address and SOCK STREAM refers to the TCP protocols
curSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

port = 80
ip = "8.8.8.8"
#getting current ip
curSocket.connect((ip,port))

# returns current ip and the port number
print( curSocket.getsockname())

curSocket.close()
