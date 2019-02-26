import time
import threading
lock=threading.Lock()
A=0
B=0
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job',A)
    lock.release


th1=threading.Thread(target=job1)
th2=threading.Thread(target=job2)
th1.start()
th2.start()
th2.join()
th1.join()
    
