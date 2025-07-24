def my_write(s):
    file = open('reply.txt', 'a', encoding='utf-8')
    file.write(s)
    file.write('\n')
    file.close()


def my_write_list(file, ls):
    f = open(file, 'a', encoding='utf-8')
    f.writelines(ls)
    f.close()


if __name__ == '__main__':
    print('请先取消注释')
    # my_write('伟大的中国梦')
    # my_write('北京欢迎您！')
    # list1 = ['姓名\t', '年级\t', '张三\t', '30\t','98']
    # my_write_list('c.txt',list1)
