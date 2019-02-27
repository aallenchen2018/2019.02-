import socket
<<<<<<< HEAD
ip_port=('192.168.4.186',9999)
while 1:
    sk=socket.socket()
    sk.connect(ip_port)
    # while 1:
    sr=input('write:   ')
    sk.sendall(('%s' %sr).encode())
    ser_reply=sk.recv(1024)
    print(ser_reply)
    sk.close()
=======
ip_port=('192.168.3.46',9988)
sk=socket.socket()
sk.connect(ip_port)

while 1:

    sr=input('enter')
    sk.sendall(('%s' %sr).encode())
    ser_reply=sk.recv(1024).decode('utf8')
    print(ser_reply)

>>>>>>> 28d8ad033d748f73604e7dd1a060ca2d925e95ec
