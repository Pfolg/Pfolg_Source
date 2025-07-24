# -*- coding: utf-8 -*-
# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 47.1_multiprocessing    ||    Author >>> Pfolg
# Date >>> 2024/6/9 and Time >>> 11:37
import time
import multiprocessing
from multiprocessing import Process
import os


def test():
    print(f'我是子进程，我的pid是：{os.getpid},我的父进程是：{os.getppid()}')
    time.sleep(1)


if __name__ == '__main__':
    print('主进程开始执行')
    list1 = []
    for i in range(5):
        # 创建子进程
        p = Process(target=test)
        p.start()
        list1.append(p)

    # 遍历list1中5个子进程
    for j in list1:# j是Process类型
        j.join()  # 阻塞主进程

    print('主进程结束')
