"""
python中的多线程无法利用多核优势，如果想要充分地使用多核CPU的资源，在python中大部分情况
需要使用多进程。Python提供了multiprocessing。

multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），
multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
"""

# 方法一 直接调用
import time
import random
from multiprocessing import Process


def run(name):
    print('%s runing' % name)
    time.sleep(5)
    print('%s running end' % name)


if __name__ == '__main__':

    p1 = Process(target=run, args=('anne',))  # 必须加,号
    p2 = Process(target=run, args=('alice',))
    p3 = Process(target=run, args=('biantai',))
    p4 = Process(target=run, args=('haha',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')
