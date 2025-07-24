# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 42_summary    ||    Author >>> Pfolg
# Date >>> 2024/6/6 and Time >>> 12:44
import random
import os
import os.path as op


# file = open('reply.txt')
# print(file)  # <_io.TextIOWrapper name='reply.txt' mode='r' encoding='cp936'>
# file.close()

# 批量创建文件
def create_name():
    filename_list = []
    list1 = ['Cat', 'Dog', 'Pig', 'Fish', 'Cow', 'Cattle', 'Duck']
    code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(1, 3001):
        filename = ''
        # 拼接文件
        if i < 10:
            filename += '000' + str(i)
        elif i < 100:
            filename += '00' + str(i)
        elif i < 1000:
            filename += '0' + str(i)
        else:
            filename += str(i)
        # 拼接文件
        filename += '_' + random.choice(list1)
        # 拼接编码
        s = ''
        for j in range(9):
            s += random.choice(code)
        filename += '_' + s
        filename_list.append(filename)
    return filename_list


def create_files(name):
    with open(name, 'w') as file:
        file.write('@Pfolg')


# 批量创建文件夹
def make_dir(p, num):
    for i in range(1, num + 1):
        os.mkdir(p + '/' + str(i))


# 记录登录日志并查看
import time


def show_info():
    a = eval(input('输入提示数字，0-退出，1-查看登录日志:'))
    return a


# 记录日志
def wl(usnm):
    with open('log.txt', 'a', encoding='utf-8') as file:  # 追加写
        s = f'用户名{usnm},登录时间{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')


# 读取日志
def read_log():
    with open('log.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line)


if __name__ == '__main__':
    # 批量创建文件
    '''
    path = 'D:\\Pyworking\\Normal\\这个是用来测试os的目录'
    if op.exists(path):
        pass
    else:
        os.mkdir(path)
    list2 = create_name()  # 存储文件名
    for it in list2:
        create_files(op.join(path, it) + '.txt')
    '''

    # 批量创建文件夹
    '''
    path = r'D:\\Pyworking\\Normal\\这个是用来测试os的目录'
    if not op.exists(path):
        os.mkdir(path)
    num = eval(input('请输入要创建目录个数:'))
    make_dir(path, num)
    '''
    # 记录用户登录日志
    user = input('user:')
    pwd = input('pwd:')
    if user == '123' and pwd == '123':
        print('login successfully!')
        wl(user)
        # 提示用户操作
        aaa = show_info()
        while True:
            if aaa == 0:
                print('ESC')
                break
            elif aaa == 1:
                print('Lading......')
                read_log()
            else:
                print('ERROR!')
            aaa = show_info()
    else:
        print('LOGIN_ERROR')
