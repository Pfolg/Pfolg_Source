# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:51:13 2024

@author: Pfolg
"""
# list_yuangong=['88','99','93','00','03','01','97']
# for i in range(len(list_yuangong)):
#     if eval(list_yuangong[i])<10:
#         list_yuangong[i]='20'+list_yuangong[i]
#     else:
#         list_yuangong[i]='19'+list_yuangong[i]
#     print(list_yuangong)
'''废了'''
# 千年虫
list_yuangong=[99,96,97,95,00,94,88]
for i in range(len(list_yuangong)):
    if list_yuangong[i]==0:
        list_yuangong[i]=eval('200'+str(list_yuangong[i] )) # 2000+list_yuangong[i]
    else:
        list_yuangong[i]=eval('19'+str(list_yuangong[i])) # 1900+list_yuangong[i] 个人觉得后面更省事
print(list_yuangong)
# 购物流程
list_goods=[]
for i in range(5):
    good=input('请输入商品编号与名称，每次只能输入一件商品：')
    list_goods.append(good)
for item in list_goods:
    print(item)
list_shop=[]
while True:
    flag=False
    shop_good=input('请输入要购买的商品编号：')
    for item in list_goods:
        if shop_good==item[0:4]:
            flag=True
            list_shop.append(item)
            print('商品已成功添加到购物车！')
            break
    if not flag and shop_good!='q': # flag==False
        print('商品不存在！')
    if shop_good=='q':
        break
print('-'*50)
print('您的购物车：')
list_shop.reverse()
for i in list_shop:
    print(i)
# 模拟购票
tain={
      'G189':['昆明西-成都东','9:30','12:50','x'],
      'G2525':['昆明西-成都南','9:53','11:48','y'],
      'C9668':['昆明西-眉山东','13:15','15:38','z'],
      'G7865':['昭通-成都东','16:51','19:02','a']
      }
print('车次    始发-终点站    开点    到点    用时')
for i in tain.keys():
    print(i,end='   ')
    for j in tain.get(i):
        print(j,end='   ')
    print()
a=input('请输入要购票的车次：')
b=tain.get(a,'车次不存在！')
if b!='车次不存在！':
    c=input('请输入乘车人：')
    d=b[0]+' '+b[1]+'开'
    print(f'{c}先生/女士 您已购买{a} '+d,'请务必准时乘车！')
else:
    print(b)
# 手机通讯录
txl=set()
for i in range(1,6):
    person=input('请输入好友的姓名+电话：')
    txl.add(person)
for j in txl:
    print(j)