##
import pandas as pd

url = 'https://pyecharts.org/#/zh-cn/'
# 可以用pandas和matplotlib或者pyecharts
import matplotlib.pyplot as plt

df = pd.read_excel('pie_example.xlsx')
# print(df)

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['Simhei']

plt.figure(figsize=(10, 6))
Labels = df['商品名称']
y = df['北京']
# print(Labels, y)
# 绘制饼图
plt.pie(y, labels=Labels, autopct='%1.1f%%')  #, startangle=90)

# 设置xy轴刻度
plt.axis('equal')
plt.title('xxxx年北京手机销量')

plt.show()
##
from pyecharts import options as opts
from pyecharts.charts import Pie
# from pyecharts.faker import Faker -->
from example.commons import Faker

# 准备数据
list1 = [['华为', 1000], ['OPPO', 1200], ['苹果', 300], ['小米', 980]]
c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("", list1)
    .set_global_opts(title_opts=opts.TitleOpts(title="xxx年北京手机销售情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("phone.html")
)
##
# print([list(z) for z in zip(Faker.choose(), Faker.values())])
# [['河马', 106], ['蟒蛇', 70], ['老虎', 146], ['大象', 150], ['兔子', 121], ['熊猫', 110], ['狮子', 73]]
