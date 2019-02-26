import socket
ip_port=('127.0.0.1',9988)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)
while 1:
    print('welcome to my server!!!')
    conn,addr=sk.accept()
    client_date=conn.recv(1024)
    print(client_date)
    conn.sendall(('server received your msg!').encode())
    conn.close()
####vscode打开时注意开另一个窗口开client
