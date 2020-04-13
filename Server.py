import socket 

host = socket.gethostname()
port = 9338

s = input("Enter Message To Send : ")

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.bind((host,port))
sock_.listen(1)

print("\nServer started...\n")

conn,addr = sock_.accept()

print("Connection established with: ",str(addr))

message = s+"\nThank you for connecting "+str(addr)
conn.send(message.encode("ascii"))

