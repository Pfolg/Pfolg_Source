import re

# match
pattern = '\d\.\d+'  # \d 0-9出现一次或多次 +限定符
print(pattern)
s = 'I study python 3.11 everyday4.25.'
match = re.match(pattern, s, re.I)  # re.I忽略大小写
print(match)
s2 = '3.11Python I study everyday.'
match2 = re.match(pattern, s2)  # match从开始位置匹配，中间找不到
print(match2)  # <re.Match object; span=(0, 4), match='3.11'>
print('-' * 50)
print('匹配值的起始位置：', match2.start())
print('匹配值的终止位置：', match2.end())
print('匹配区间的元素位置：', match2.span())
print('待匹配的字符串：', match2.string)
print('匹配的数据：', match2.group())
# search
print('-' * 50)
match3 = re.search(pattern, s)
print(match3)  # <re.Match object; span=(15, 19), match='3.11'> 只能找到第一个
s3 = 'Python I study everyday.'
match4 = re.search(pattern, s3)
print(match4)  # None
print(match3.group())
# print(match4.group())
# findall
list1 = re.findall(pattern, s)  # 查找所有
print(list1)  # ['3.11', '4.25']
list2 = re.findall(pattern, s3)
print(list2)  # []

# sub&split
str1 = '黑客|反爬|破解'
str2 = '我想学习Python，用来破解VIP视频，那可以无限制反爬吗？'
str3 = re.sub(str1, '*', str2)
print(str3)

str4 = 'https://www.csdn.net/?ydreferer=aHR0cHM6Ly9jbi5iaW5nLmNvbS8%3D'
str5 = '[?|%|/]'
str6 = re.split(str5, str4)
print(str6)

# 数据验证的方法
print('123'.isdigit())  # true 0-9的阿拉伯数字
print('一二三'.isdigit())  # false
print('123'.isnumeric())  # true
print('0b01010111'.isnumeric())  # true
print('-' * 50)
print('hello你好'.isalpha())  # True都是字母
print('hello你好666'.isalpha())  #false
print('*' * 50)
print('svhfbgjhsfb4546468'.isalnum())  # true
print('hellow'.islower())  # true
print('Hello'.isupper())  # false
print('*' * 50)
print('Hello'.istitle())  # 首字母都大写 true
print("Hello World".istitle())  # true
print(' \t\n'.isspace())  # true空白字符串
