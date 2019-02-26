import time
import threading
def t1():
    print('T1开始了')
    for i in range(10):
        time.sleep(0.1)
    print('T1结束了')

def t2():
    print('t2开始了')
    print('t2结束了')

th1=threading.Thread(target=t1)
th2=threading.Thread(target=t2)
th1.start()
th2.start()
th2.join()
th1.join()

print('finished')

