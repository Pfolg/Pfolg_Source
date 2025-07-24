# -*- coding: utf-8 -*-
# Project >>> chaoxing.py   ||    Environment >>> PyCharm
# FileName >>> 49_restud    ||    Author >>> Pfolg
# Date >>> 2024/6/11 and Time >>> 21:48
import re
str = 'Hello1ooo123Python!'

pat = '^He..'     #pat为正则表达式
result = re.search(pat, str)
print(result)

pat2 = '..on!$'     #pat2为正则表达式
result = re.search(pat2, str)
print(result)

pat3 = '1o*'     #pat3为正则表达式
result = re.search(pat3, str)
print(result)

pat4 = 'e.*'     #pat4为正则表达式
result = re.search(pat4, str)
print(result)

pat5 = '1o{4}'     #pat5为正则表达式
result = re.search(pat5, str)
print(result)

pat6 = 'o(\d*?)P'
result = re.compile(pat6).findall(str)
print(result)

#结果：
# <re.Match object; span=(0, 4), match='Hell'>
# <re.Match object; span=(14, 19), match='thon!'>
# <re.Match object; span=(5, 9), match='1ooo'>
# <re.Match object; span=(1, 19), match='ello1ooo123Python!'>
# None
# ['123']
