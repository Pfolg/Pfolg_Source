## 使用类计算圆的C&S
import math


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        S = self.r ** 2 * math.pi
        print('圆的面积为：{:.2f}'.format(S))

    def get_perimeter(self):
        C = self.r * math.pi * 2
        print('圆的周长为：{:.2f}'.format(C))


r = Circle(r=eval(input('请输入圆的半径：')))
r.get_area()
r.get_perimeter()


## 输入五位学生信息：（姓名#年龄#性别#成绩）并打印在屏幕上
class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def infor(self):
        print(self.name, self.age, self.gender, self.score)


print('请输入五位学生信息：（姓名#年龄#性别#成绩）')
list1 = []
for i in range(5):
    s = input(f'请输入第{i + 1}位学生信息及成绩：')
    list2 = s.split('#')
    stu = Student(list2[0], list2[1], list2[2], list2[3])
    list1.append(stu)

for i in list1:
    i.infor()


## 乐器弹奏（感觉像放屁）
class Instrument():
    def make_sound(self):
        pass


class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')


class Piano(Instrument):
    def make_sound(self):
        print('钢琴在弹奏')


class Violin(Instrument):
    def make_sound(self):
        print('小提琴在弹奏')


def play(obj):
    obj.make_sound()


er = Erhu()
piano = Piano()
violin = Violin()

play(er)
play(piano)
play(violin)


##  车车，嘿嘿
class Car:
    def __init__(self, info, num):
        self.info = info
        self.num = num

    def start(self):
        pass

    def end(self):
        pass


class Taxi(Car):
    def __init__(self, company, info, num):
        self.company = company
        super().__init__(info, num)

    def start(self):
        print(f'乘客您好，\n我是{self.company}的，我的车牌是：{self.num}，您要去哪里？')

    def end(self):
        print('目的地到了，请您付款下车，欢迎下次乘坐！')


class Private_Car(Car):
    def __init__(self, owner, info, num):
        super().__init__(info, num)
        self.owner = owner

    def start(self):
        print(f'我是{self.owner}，我的车车我来开，嘿嘿！')

    def end(self):
        print('目的地到了，快滚下车去！！！')


taxi = Taxi('长峰运输', '奥迪', '川Q12345')
pri = Private_Car('张三', '比亚迪', '川A66666')
taxi.start()
taxi.end()
print('-'*50)
pri.start()
pri.end()
##
