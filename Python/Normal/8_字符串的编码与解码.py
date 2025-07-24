# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:55:26 2024

@author: 21460
"""
str1 = '我爱高数'
code1 = str1.encode(errors='replace')  # utf-8
print(code1)  # b'\xe6\x88\x91\xe7\x88\xb1\xe9\xab\x98\xe6\x95\xb0' utf-8中文占3个字符
code_gbk = str1.encode('gbk', errors='replace')
print(code_gbk)  # \xce\xd2\xb0\xae\xb8\xdf\xca\xfd' gbk中中文占2个字符
str2 = '哈哈哈☺☺☺'
code2 = str2.encode('gbk', errors='ignore')
print(code2)  # b'\xb9\xfe\xb9\xfe\xb9\xfe'
# code3=str2.encode('gbk',errors='strict')
# print(code3) # 直接报错 'gbk' codec can't encode character '\u263a' in position 3: illegal multibyte sequence
code3 = str2.encode('gbk', errors='replace')
print(code3)  # b'\xb9\xfe\xb9\xfe\xb9\xfe???'
print('-' * 50)
print(bytes.decode(code2, 'gbk'))  # 哈哈哈
print(bytes.decode(code1, 'utf-8'))  # 我爱高数
print('你好呀！'.encode('gbk', errors='replace'))
print('-' * 50)
str3 = 'hello'
str4 = 'world'
print(str3 + str4)
# 使用join()
print(''.join([str3, str4]))
print('abab'.join(['可莉', '刻晴', '宵宫', '搜狗', '充电宝']))  # 可莉abab刻晴abab宵宫abab搜狗abab充电宝
# 直接拼接
print('hello''world')  # helloworld
# 使用格式化字符串
print('%s%s' % ('hello', 'world'))  # helloworld
print(f'{str3} {str4}')
print('{0}{1}'.format(str3, str4))  # 占位符 helloworld
# 去重 遍历
str5 = 'fnbwgbfyuwgbfeWHGBYEGFDFHavCFGHkqweDFYTWFAWGDUJQgwauyegfrrukwyagrfuywagtw'
str6 = str5.lower()
str7 = ''
for i in str6:
    if i not in str7:
        str7 += i
    else:
        pass
print(str7)  # fnbwgyuehdavckqtjr
# 去重 索引
str8 = ''
for i in range(len(str6)):
    if str6[i] not in str8:
        str8 += str6[i]
    else:
        pass
print(str8)
print(str7 == str8)  # True
# 通过集合去重+列表
middle_variable = set(str6)
list1 = list(middle_variable)
print(list1)  # ['n', 'y', 'h', 'a', 'c', 'f', 'q', 'j', 'k', 'd', 'e', 't', 'u', 'v', 'b', 'g', 'r', 'w']
list1.sort(key=str6.index)
print(''.join(list1))  # fnbwgyuehdavckqtjr
