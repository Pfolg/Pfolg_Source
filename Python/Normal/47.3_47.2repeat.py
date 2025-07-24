# -*- coding: utf-8 -*-
# Project >>> Pfolg   ||    Environment >>> PyCharm
# FileName >>> 47.3_47.2repeat    ||    Author >>> Pfolg
# Date >>> 2024/6/10 and Time >>> 22:41
from multiprocessing import Process
import os, time


# 函数式方式创建子进程
def sub_process(name):
    print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()},__________________{name}')
    time.sleep(1)


def sub_process2(name):
    print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()},__________________{name}')
    time.sleep(1)


if __name__ == '__main__':
    # 主进程
    print('主进程开始')
    for i in range(5):
        p1 = Process(target=sub_process,args=('Pfolg',))
        p2 = Process(target=sub_process2,args=(18,))  # 没有参数调父类run()方法

        p1.start()
        p2.start()  # 如果指定了参数，Process会调用指定的函数执行

        # 强制终止
        # p1.terminate()
        # p2.terminate()
    print('主进程执行完毕')
