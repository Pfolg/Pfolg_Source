import os.path as op

print('获取文件或目录的绝对路径：', op.abspath('.\\41.3_目录&文件.py'))
print('判断文件和目录在磁盘上是否存在：', op.exists('reply.txt'))
print('判断文件和目录在磁盘上是否存在：', op.exists('new_b.txt'))
print('判断文件和目录在磁盘上是否存在：', op.exists('..\\Normal'))
print('拼接路径：', op.join(r'D:\Pyworking\Normal', 'reply.txt'))
print('分割文件的名和后缀名：', op.splitext('reply.txt'))  # 元组
print('提取文件名：', op.basename(r'D:\Pyworking\Normal\b.txt'))
print('提取路径：', op.dirname(r'D:\Pyworking\Normal\b.txt'))

print('-' * 50)
print('判断一个路径是否为有效路径：', op.isdir(r'D:\Pyworking\Normal\b.txt'))  # False
print('判断一个路径是否为有效路径：', op.isdir(r'D:\Pyworking\Normal'))  # True
print('判断文件是否有效：', op.isfile(r'/Normal/reply.txt'))  # True
print('判断文件是否有效：', op.isfile(r'D:\Pyworking\Normal\bcd.txt'))  # False
