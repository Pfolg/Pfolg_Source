# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   05_进度条tqdm |User    Pfolg
# 2024/7/10   20:19
import time
import tqdm


class Practice:
    def __init__(self):
        pass

    def study1(self):
        for _ in tqdm.tqdm(range(10000), desc="待定字符串"):
            time.sleep(0.001)

    def study2(self):  # 好像不能用
        for _ in tqdm.tgrange(10000):
            time.sleep(0.001)

    def middle1(self):
        for i in range(50):
            yield i

    def study3(self):
        for _ in tqdm.tqdm(self.middle1()):
            time.sleep(0.5)

    def study4(self):
        for _ in tqdm.tqdm(self.middle1(), total=50):
            time.sleep(0.5)


def pbar_inter():
    pbar = tqdm.tqdm(total=1000)
    pbar.update(10)
    time.sleep(1)
    pbar.update(100)
    time.sleep(3)
    pbar.update(500)
    time.sleep(5)
    pbar.update(390)
    pbar.close()


if __name__ == '__main__':
    x = Practice()
    # x.study1()  # 命令行，实现效果不错
    # x.study2()  # 独立窗口
    # x.study3()  # 对于未知时间的进度条
    x.study4()
    # pbar_inter()
