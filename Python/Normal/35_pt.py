import prettytable as pt


def show_ticket(r):
    tb = pt.PrettyTable()  # 创建一张表格
    # 设置标题
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    # 遍历有票
    for i in range(1, r + 1):
        list1 = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(list1)
    print(tb)


# 订票
def order_ticket(r, r1, co):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(1, r + 1):
        if int(r1) == i:
            list1 = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            list1[int(co)] = '已售'
            tb.add_row(list1)
        else:
            list1 = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(list1)
        print(tb)


if __name__ == '__main__':
    r = 6

    show_ticket(r)

    choose_num = input('请输入您选择的座位 eg.4,3 表示4行3列:')
    r1, co = choose_num.split(',')  # 系列解包赋值
    order_ticket(r, r1, co)
