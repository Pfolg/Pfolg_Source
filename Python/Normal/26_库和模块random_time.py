##
import random

random.seed(4654)  # 给了这个就相当于不随机了，寄几领悟
a = random.randint(1, 101)
b = random.uniform(a=-6, b=6)
c = random.random()  # [0.0,1.0]
print(a, '\n', b, '\n', c)

for i in range(10):  # 含开始不含结束
    print(random.randrange(0, 101, 5), end=' ')
print('-' * 50)
# 随机排序
list1 = [random.randint(1, 101) for i in range(10)]
print(list1)
print(random.choice(list1))  # 随便选一个
random.shuffle(list1)  # 随机排序
print(list1)
random.shuffle(list1)
print(list1)
##  time
import time

now = time.time()
print(now)

obj = time.localtime()
print(obj)

obj2 = time.localtime()  # 60s
print(obj2)
print(type(obj2))
print('年：', obj2.tm_year)
print('月：', obj2.tm_mon)
print('日：', obj2.tm_mday)
print('时：', obj2.tm_hour)
print('分：', obj2.tm_min)
print('秒：', obj2.tm_sec)
print('星期：', obj2.tm_wday)  # [0,6]
print('今年的第几天：', obj2.tm_yday)
print(time.ctime())
print('-' * 50)
print(time.strftime('%Y-%m-%d', time.localtime()))
print(time.strftime('%H:%M:%S', time.localtime()))
print(time.strftime('%A星期的名称', time.localtime()))
print(time.strftime('%B月份的名称', time.localtime()))
# 字符串转struct_time
print('字符串转struct_time:', time.strptime('2024-5-22', '%Y-%m-%d'))
time.sleep(20)  # 程序暂停20s
print('-' * 50)
print('****字符串转struct_time2 ', time.strptime('2024-5-22 10:33:57', '%Y-%m-%d %H:%M:%S'))
##  datetime
import datetime

print('当前的系统时间:', datetime.datetime.now())  # 当前的系统时间
print(datetime.time)
dt2 = datetime.datetime(2028, 8, 6, 6, 6, 33, 67)
print('dt2的数据类型：', type(dt2), '具体为:', dt2)
print(f'年：{dt2.year}\n月：{dt2.month}\n日：{dt2.day}\n时：{dt2.hour}\n分：{dt2.minute}\n秒：{dt2.second}\n{"-" * 50}')
# 还可以比大小
dt1 = datetime.datetime.now()
print(dt2 > dt1)
# 可以和字符串转换
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'now的数据类型{type(now)},\nnow_str的数据类型{type(now_str)},输出为{now_str}')
str_time = '2030年5月22日10:57:16'
time_time = datetime.datetime.strptime(str_time, '%Y年%m月%d日%H:%M:%S')
print(f'{"-" * 50}\n', time_time, '的数据类型为：', type(time_time))
# timedelta
# 创建两个datetime对象
t1 = datetime.datetime(2028, 10, 1) - datetime.datetime(2024, 5, 22)
print('\nt1的数据类型为', type(t1), '\n表示的数据：', t1)
t2 = datetime.datetime(2024, 5, 22) + datetime.timedelta(days=1593)
print('\nt1的数据类型为', type(t2), '\n表示的数据：', t2)

