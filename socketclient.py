import socket
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
