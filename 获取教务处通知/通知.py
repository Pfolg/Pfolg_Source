# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   通知 |User    Pfolg
# 2024/7/10   21:03
import re
import requests
import prettytable

url = "https://jwc.cuit.edu.cn/"

a = requests.get(url)
a.encoding = "utf-8"
b = a.text
# print(b)

c = re.findall("<H5 class=\"col_5\"><A href=\"(.*)\" target=\"_blank\" style=\"color: #ff6a6a\">(.*)</A></H5>", b)
d = re.findall("<H6 style=\"color: #ff6a6a\">(.*)</H6>", b)
# print(c, d)
e = re.findall("<H5 class=\"col_5\"><A href=\"(.*)\" target=\"_blank\">(.*)</A></H5>", b)
f = re.findall("<H6>(.*)</H6>", b)

table = prettytable.PrettyTable()
table.field_names = ["时间", "链接", "标题"]
for i in range(len(c)):
    table.add_row([d[i], f"{url}" + c[i][0], c[i][1]])

table.add_row(["-", "-", "-"])

for k in range(len(e)):
    table.add_row([f[k], f"{url}" + e[k][0], e[k][1]])

print(table)
print("上半部分是学校标红的通知，下半部分是蓝色的通知")