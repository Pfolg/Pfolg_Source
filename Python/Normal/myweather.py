# 这个文件属于29.1
import requests
import re


def get_html():
    url = 'http://www.weather.com.cn/weather1d/101010100.shtml'
    req = requests.get(url)
    # 设置一下编码格式
    req.encoding = 'utf-8'
    print(req.text)
    return req.text


def parse_html(html_str):
    city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', html_str)
    weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', html_str)
    wd = re.findall('<span class="wd">(.*)</span>', html_str)
    zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', html_str)
    list1 = []
    for a, b, c, d in zip(city, weather, wd, zs):
        list1.append([a, b, c, d])
        print(list1)
    return list1
'[\u4e00-\u9fa5]'
