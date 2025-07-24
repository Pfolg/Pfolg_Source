# 高维数据的存储
import json

list1 = [
    {'name': 'Pfolg', 'age': 18, 'score': 100},
    {'name': '郑三', 'age': 19, 'score': 98},
    {'name': '张三', 'age': 20, 'score': 98}
]
#
print('step', 1)
s = json.dumps(list1, ensure_ascii=False, indent=4)  # ensure_ascii正常显示中文，indent增加数据的缩进，使json更具有可读性
print(type(s))  # 编码 list-->str,列表中是字典
print(s)

# 解码
print('step', 2)
list2 = json.loads(s)
print(type(list2))
print(list2)

# 编码到文件中
with open('studentjson.txt', 'w') as file:
    json.dump(list1, file, ensure_ascii=False, indent=4)

# 解码到文件
with open('studentjson.txt', 'r') as file:
    list3 = json.load(file)
    print(type(list3))
    print(list3)
