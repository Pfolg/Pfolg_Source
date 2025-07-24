class Student:
    # 类属性，定义在类中，方法外变量
    school = 'cuit'

    # 初始化方法
    def __init__(self, xm, age):  # xm age 是参数，局部变量，作用域是整个__init__方法
        self.name = xm  # =左侧是实例属性，将局部变量的值赋值给实例属性self.name
        self.age = age  # 实例属性的名称可以和局部变量的名称相同

    # 实例方法——定义在类中的函数称为方法，自带一个self参数
    def show(self):
        print(f'my name is {self.name},my age is {self.age}')


# 根据图纸可以创建N多个对象
stu = Student('Pfolg', 18)
stu2 = Student('lny', 19)
stu3 = Student('僚机', 1)
stu4 = Student('Marry', 19)
print(type(stu))
print(type(stu2))
print(type(stu3))
print(type(stu4))

Student.school = 'cuit'
# list1 = [stu, stu2, stu3, stu4]
# for i in list1:
#     i.show()  # 对象名打点调用

print(stu.name, stu.age)
stu2.gender = '男'  # 动态绑定一个实例属性
print(stu2.age, stu2.name, stu2.gender)


# print(stu.gender)  # AttributeError: 'Student' object has no attribute 'gender'
# 动态绑定方法
def introduce():
    print('我是一个可爱的函数，但是被动态绑定给了stu4，于是我变成了stu4的专属函数！！！')


stu4.fun = introduce  # 函数的赋值，不能加括号
stu4.fun()  # 打点调用
