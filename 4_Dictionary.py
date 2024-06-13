# Dictionary
st_r = {'a': 1, 'b': 9}
dict_1 = {'height': 180, 100: 'full score', 'student': [185, 'name', 'score'], \
          'phrase': 'I am here'}
print(dict_1)
student_room = {'Emma': 309, 'Jack': 582, "Olivia": 764}
student_room_2 = {'Jack': 582, 'Emma': 309, 'Olivia': 764}
print(student_room == student_room_2)  #字典不区分元素位置
print(student_room.keys())
print(student_room.values())
for i in student_room:
    print(i, student_room[i])
for key in student_room:
    print(key, student_room[key])
print('-' * 50)
del student_room_2['Olivia']
# student_room_2.pop('Olivia')#这一行和上一行等效
print(student_room_2)
student_room_2.clear
print(student_room_2)
# tuples 不可变（元组）
tupple_A = (10, 20.01, 'A string', {'Asia': 'China'}, [1, 2, 3])
print(type(tupple_A))
print(tupple_A)

# set 集合
set1 = set('ssssssssi')
print(set1)
set3 = set([1, 2, 3, 4])
set4 = set([3, 4, 5, 6])
print(set3 - set4)
print(set3 & set4)
print(set3 | set4)


# 用户定义函数：同一py.文件
def my_add(variable_1, variable_2):
    a = variable_1 + variable_2
    return a  #形式参数


v1 = 2
v2 = 3
a = my_add(v1, v2)  #实际参数
print(f"my_add function:{v1}+{v2}={a}")
