# -*- coding: utf-8 -*-
# Project >>> make_pie.py   ||    Environment >>> PyCharm
# FileName >>> 50_进度条    ||    Author >>> Pfolg
# Date >>> 2024/6/13 and Time >>> 18:37
import time

from alive_progress import alive_bar
from tqdm import trange
from progressbar import ProgressBar, Percentage, Bar, Timer, ETA, FileTransferSpeed


# 假设需要执行100个任务
def jdt1():
    s = 0
    with alive_bar(100) as bar:
        for item in range(100):  # 遍历任务
            s += item
            time.sleep(0.5)
            bar()  # 显示进度


def jdt2():
    for i in range(101):
        mid = '*' * i + ('-' * (100 - i))
        print(f'\r\033[38;2;0;242;255m{mid}\033[0m', f'{i}%', end='')
        time.sleep(0.5)


def jdt3():
    s = 0
    for i in trange(100):
        s += i
        time.sleep(.05)  # 有用


def jdt4():
    s = 0
    widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(), ' ', ETA(), ' ', FileTransferSpeed()]
    progress = ProgressBar(widgets=widgets)
    for i in progress(range(100)):
        s += i
        time.sleep(0.05)


if __name__ == '__main__':
    # jdt1()
    jdt3()
