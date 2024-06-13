input_value = input('Please input H_wind_speed')
if input_value.isdigit():
    v = float(input_value)
    if v < 33:
        print('NULL')
    elif v >= 33 and v < 42:
        print('level 1')
    elif v >= 42 and v < 49:
        print('level 2')
    elif v >= 49 and v < 58:
        print('level 3')
    elif v >= 58 and v < 70:
        print('level 4')
    else:
        print('leve 5')

i = 0
while i < 10:
    print(i)
    i = i + 1  #给i赋值
print('循环结束！')

i = 0
b = 0
while i < 100:
    i = i + 1
    b = b + i
print(b / 100)

#while循环

i = 1
s = 0
while i < 101:
    s = s + i
    i = i + 1
print(s)

#for循环

for i in range(2, 10, 1):  #range(起始值，终止值，分度值—-大概吧)
    print(i)

sum = 0
for i in range(0, 101, 1):
    sum = sum + i
print(sum)
