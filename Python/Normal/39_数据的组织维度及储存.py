'''
一维数据    列表、元组、集合
二维数据    行和列，二维列表
高维数据    key-value字典、json模块
'''


# 一维数据
def my_write():
    list1 = ['张三', '李四', '王五', '柽柳', '马琪']
    with open('student.csv', 'w') as file:
        file.write(','.join(list1))  # 使用，进行拼接


def my_read():
    with open('student.csv', 'r') as file:
        s = file.read()
        list1 = s.split(',')
        print(list1)


# 二维数据
def my_write_table():
    list1 = [
        ['商品名称', '单价', '采购数量'],
        ['水杯', '98', '20'],
        ['鼠标', '50', '12'],
    ]
    with open('table.csv', 'w', encoding='utf-8') as file:
        for i in list1:
            line = ','.join(i)
            file.write(line)
            file.write('\n')


def my_read_table():
    data = []
    with open('table.csv', 'r', encoding='utf-8') as file:
        list1 = file.readlines()
        # print(type(list1), list1)
        for i in list1:
            list2 = i[:len(i) - 1].split(',')
            data.append(list2)
    print(data)  # [['商品名称', '单价', '采购数量'], ['水杯', '98', '20'], ['鼠标', '50', '12']]


if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()
