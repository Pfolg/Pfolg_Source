import requests
import re

url = 'http://www.weather.com.cn/weather1d/101010100.shtml'
req = requests.get(url)
# 设置一下编码格式
req.encoding = 'utf-8'
print(req.text)
'[\u4e00-\u9fa5]'
city = re.findall('<span class="name">(.*)</span>', req.text)
weather = re.findall('<span class="weather">(.*)</span>', req.text)
wd = re.findall('<span class="wd">(.*)</span>', req.text)
zs = re.findall('<span class="zs">(.*)</span>', req.text)
# print(city)
# print(weather)
# print(wd)
# print(zs)
list1 = []
for a, b, c, d in zip(city, weather, wd, zs):
    list1.append([a, b, c, d])
for i in list1:
    print(i)
'''<span class="name">三亚</span>
<span class="weather">雷阵雨</span>
<span class="wd">31/25℃</span>
<span class="zs">一般</span>'''
