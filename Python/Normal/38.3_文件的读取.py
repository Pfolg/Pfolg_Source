def my_read(file):
    f = open(file, 'w+', encoding='utf-8')
    f.write('哈喽啊！')  # 写入完成后，文件的指针在str后
    # seek 修改指针位置
    f.seek(0)
    # 读取
    # s = f.read()  # 读取全部
    # s=f.read(2)  # 两个字符
    # s=f.readline()  # 读取一行
    # s=f.readline(2)  # 读取一行中两个字符
    # s = f.readlines()  # 读取所有，一行为列表中的一个元素 s为一个列表
    f.seek(3)
    s=f.read()  # <class 'str'> 喽啊！
    print(type(s), s)
    f.close()


if __name__ == '__main__':
    my_read('d.txt')
