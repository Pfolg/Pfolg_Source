import datetime


def input_date():
    date_in = input('请输入开始日期（20281001后回车）：')
    datestr = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:]
    # 类型转换
    dt = datetime.datetime.strptime(datestr, '%Y-%m-%d')
    return dt


# 主程序运行
if __name__ == '__main__':
    date = input_date()
    # 输入间隔的天数
    in_num = eval(input('请输入间隔天数:'))
    date = date + datetime.timedelta(days=in_num)
    print(f'您推算的日期是：{date}')
