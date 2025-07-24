# -*- coding: utf-8 -*-
# Project >>> Pfolg   ||    Environment >>> PyCharm
# FileName >>> 47.2_Process常用    ||    Author >>> Pfolg
# Date >>> 2024/6/10 and Time >>> 22:20
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
    print('父进程开始执行')
    for i in range(5):
        # 创建第一个子进程
        p1 = Process(target=sub_process, args=('Pfolg',))
        # 2
        p2 = Process(target=sub_process2, args=(18,))

        # 调用start（）
        p1.start()
        p2.start()
        print(p1.name, '是否执行完毕：', p1.is_alive)
        print(p2.name, '是否执行完毕：', p2.is_alive)

        print(p1.name, 'PID:', p1.pid)
        print(p2.name, 'PID:', p2.pid)

        p1.join()
        p2.join()  # 主进程要等待p2执行完毕
        # 去掉join后子进程随机执行
    print('父进程执行完毕')