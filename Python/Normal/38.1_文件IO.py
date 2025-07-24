def my_write():
    # 打开（创建）文件
    flie = open('a.txt', 'w', encoding='utf-8')
    # 操作文件
    flie.write('测试写作')
    # 关闭
    flie.close()


def my_read():
    file = open('a.txt', 'r', encoding='utf-8')
    s = file.read()
    print(type(s), s)
    file.close()


if __name__ == '__main__':
    my_write()
    my_read()


'''
r   以只读模式打开，指针在文件开头，如果文件不存在，报错
rb  以只读模式打开二进制文件，如图片
w   覆盖写模式，文件不存在则创建，有则覆盖
wb  覆盖写模式，二进制，同上
a   追加写模式，文件不存在则创建，有则在文件后加内容
+   与w/r/a一起使用，在原功能的基础上同时加上读写功能
'''