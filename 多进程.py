#多进程作用是弥补threading中的gil锁问题
#添加进程  运用是定义main的函数语句
#(if __name=='__main__') 以下的代码
#1.作为脚本运行 
#2.作为模块不运行

#栗子
import multiprocessing as mp 
def job(a,d):
    print(a+d) 
if __name__=='__main__':
    pl=mp.Process(target=job,args=(2,4))
    pl.start()
    pl.join()

###
