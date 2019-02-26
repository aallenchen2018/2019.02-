import socket
ip_port=('192.168.3.46',9988)
sk=socket.socket()
sk.connect(ip_port)

while 1:

    sr=input('enter')
    sk.sendall(('%s' %sr).encode())
    ser_reply=sk.recv(1024).decode('utf8')
    print(ser_reply)

