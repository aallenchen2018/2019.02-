import socket
ip_port=('127.0.0.1',9988)
sk=socket.socket()
sk.connect(ip_port)
sk.sendall(('im client!').encode())
ser_reply=sk.recv(1024)
print(ser_reply)
sk.close()
