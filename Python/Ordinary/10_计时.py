# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   10_计时 |User    Pfolg
# 2024/7/16   0:33
import time

start_time = time.perf_counter()

# 假设这里有一些操作需要计时
time.sleep(5)

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print("时间差：", int(elapsed_time), "秒")