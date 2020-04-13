import socket

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.connect((socket.gethostname(),9338))
msg = sock_.recv(20024)
sock_.close()
print(msg.decode("ascii"))
