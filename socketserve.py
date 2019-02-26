import socket
import threading
ip_port=('192.168.3.46',9988)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)

def handle_sock(sock,addr):
    while 1:
        client_date=conn.recv(1024)
        print(client_date.decode('utf8'))
        re_data=input('enter:  ')
        conn.send(re_data.encode('utf8'))

while 1:
    conn,addr=sk.accept()
    
    #用线程去处理新接受的连接(用户)
    client_thread=threading.Thread(target=handle_sock,args=(conn,addr))
    client_thread.start()

    # client_date=conn.recv(1024)
    # print(client_date.decode('utf8'))
    # re_data=input('enter:  ')
    # conn.send(re_data.encode('utf8'))

####vscode打开时注意开另一个窗口开client
