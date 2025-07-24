def describle_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}\n")


describle_pet(pet_name='kiki')
print('\\')
print('-' * 50)
# 文件打开
print('*' * 50)
f1 = open('D:\\Work\\大一下\\Python\\Class\\test_1.txt', 'w')  # D:\\Work\\大一下\\Python\\Class\\test_1.txt-->.\\test_1
print(f1.name, ',', f1.mode)
print('是否关闭', f1.closed)
print('类型：', type(f1))
f1.close()
print('是否关闭', f1.closed)
# 文件关闭-使用with自动关闭文件
with open('test_1.txt', 'w') as f3:
    print(f3.name, ',', f3.mode)
    print('是否关闭', f3.closed)
    print('是否关闭', f3.closed)
print('是否关闭', f3.closed)

import os

current_path = os.getcwd()  # 获取当前路径
print(current_path)
my_path = current_path + '\\files'
print(my_path)
os.mkdir(my_path)  # 当前文件夹下建立files文件夹
f = open('.\\files\\no1.txt', 'w')
f.close()  # 创建并关闭文件
f = open('.\\files\\no2.txt', 'w')
f.close()
f = open('.\\files\\no3.txt', 'w')
f.close()
all_file_name = os.listdir(path='.\\files')
print('所有文件的文件名：', all_file_name)
# read
f = open('.\\read_test_1.txt', 'r', encoding='utf-8')
aa = f.readline()
print(aa)
aa = f.readline()
print(aa)
aa = f.read(2)
print(aa)
aa = f.read(3)
print(aa)
aa = f.read(6)  # 震惊！提行算一个字符
print(aa)
f.close()
# write
f = open('.\\write_test_1.txt', 'w')
f.write('第一行：写文件')
f.write('\nsecond line:write file')
f.close()
print('-' * 50)
f = open('.\\write_test_2.txt', 'w')
f.writelines(['1', '2', '3'])
f.writelines(['\n', '\n', '\n'])
f.close()
# seek tell
# print('-' * 50)
# f = open()
