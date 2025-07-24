##
from PIL import Image

#加载图片
im = Image.open('google.png')
# print(type(im), im)
# 提取RGB
r, g, b = im.split()
# print(r,g,b)
# 合并
om = Image.merge(mode='RGB', bands=(r, b, g))
# om.save('new_google.png')
##
import jieba
import pdfplumber

txt = ''
with pdfplumber.open('小学数学公式.pdf') as pdf:
    for i in pdf.pages:
        txt += i.extract_text()
# print(txt)
# eg.
with open('shuju.txt', 'r', encoding='utf-8') as file:
    s = file.read()

list2 = jieba.lcut(s)
# print(list2)
# 文本去重 集合
set1 = set(list2)
# 统计
d = {}
for i in set1:
    if len(i) >= 2:
        d[i] = 0

# print(d)
new_list = []
for i in list2:
    if i in d:
        d[i] = d.get(i) + 1

# print(d)
for i in d:
    new_list.append([i, d[i]])
# print(new_list)
new_list.sort(key=lambda x: x[1], reverse=True)
# print(new_list[0:10])  # 显示前十项
##
import pyecharts.options as opts
from pyecharts.charts import WordCloud

(
    WordCloud()
    .add(series_name="小学数学资料分析", data_pair=new_list, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="小学数学资料分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("basic_math.html")
)
print("ok")
##