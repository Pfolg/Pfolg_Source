# except结构
##
try:
    num1 = float(input('被除数num1='))
    num2 = float(input('除数num2='))
    result = num1 / num2
except ZeroDivisionError:  # ZeroDivisionError: float division by zero
    print('除数为0！')
except ValueError:  # ValueError: could not convert string to float: 'a'
    print('变量异常！')
except BaseException:
    print('未知异常！')
else:  # 程序无异常所执行的代码
    print('result=', result)
finally:
    print('这是无论如何都要执行的代码')
##
try:
    gender = input('your gender=')
    if gender != '男' and gender != '女':
        raise Exception('你是不男不女吗？')
    else:
        print('your gender is ' + gender)
except Exception as a:
    print(a)
##
i = 0
while i < 11:
    i += 1
    print(i)
##
try:
    score = float(input('your score='))
    if score > 100 or score < 0:
        raise Exception('您输入的可能不是一个成绩！')
    if score <= 50:
        raise Exception('您的绩点为0')
    else:
        print('您的绩点为 ' + str((score - 50) / 10))
except Exception as a:
    print(a)
finally:
    print('绩点计算结束！')
##  # 随便写的一个程序，没想到能跑
