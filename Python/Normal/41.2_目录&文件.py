import os

# 删文件
try:
    os.remove('.\\a.txt')  # 二次执行报错
    os.rename('.\\aa.txt', '.\\new_aa.txt')
except FileNotFoundError:
    pass

# 转换时间格式
import time


def date_format(longtime):
    s = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(longtime))
    return s


# 获取文件信息
in1 = os.stat('.\\new_aa.txt')

print(type(in1), in1)

print('最近一次访问时间:', date_format(in1.st_atime))
print('在windows系统中显示的文件创建时间为：', date_format(in1.st_ctime))
print('最后一次修改时间：', date_format(in1.st_mtime))
print('文件的大小（字节）：', in1.st_size)

# 启动路径下的文件
# os.startfile('calc.exe')  # 打开计算器
# 启动python解释器
# os.startfile(r"C:\Users\21460\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\IDLE (Python 3.12 64-bit).lnk")
os.startfile(r'D:\Pyworking\Pygame_study\Mines_Cleaner\Mines_Cleaner.exe')
