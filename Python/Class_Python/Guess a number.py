import random

a = random.randint(1, 10)
x = 11
y = 0
for i in range(3):
    b = int(input("Enter a number: "))
    y += 1
    if b == a:
        print("恭喜您，回答正确！！！")
        break
    elif y == 3:
        print('对不起，您没有机会了！')
        break
    elif b > a:
        print(f"您的数字大了，您还有{3 - y}次机会！")
        continue
    elif b < a:
        print(f'您的数字小了，您还有{3 - y}次机会！')
        continue
    else:
        print('error!')  # 希望这一步永远不会被执行
