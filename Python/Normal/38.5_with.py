# with open('') as file:
#     pass
def write_fun():
    with open('aa.txt', 'w', encoding='utf-8') as file:
        file.write('2022北京冬奥会')


def read_fun():
    with open('aa.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def copy(old, new):
    with open(old, 'r', encoding='utf-8') as file:
        with open(new, 'w', encoding='utf-8') as file2:
            file2.write(file.read())  # 将读取的内容直接写进去


if __name__ == '__main__':
    write_fun()
    read_fun()
    copy('.\\aa.txt', '.\\bb.txt')
# 运行了之后好像没有效果
