##
a = 1
b = 1.1
c = '一'
print('a=', type(a))  # a= <class 'int'>
print('b=', type(b))  # b= <class 'float'>
print('c=', type(c))  # c= <class 'str'>


##
# 自定义类
# 对象名=类名()
class Teacher:
    pass


yy = Teacher()


class Launage():
    pass


python = Launage()


class Software:
    pass


QQ = Software()


class Class:
    pass


experiment = Class()


print('yy=', type(yy), '\npython=', type(python), '\nQQ=', type(QQ), '\nexperiment=', type(experiment))


##
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

    # 静态方法  不会自带self
    @staticmethod
    def su():
        # print(self.name)  # 报错
        # print(self.show())  # 报错
        print('这是一个静态方法，不能调用实例属性和实例方法')

    @classmethod
    def cm(cls):
        print('这是一个类方法，不能调用实例属性和实例方法')


print('目前还无法使用这个类，要先创建对象')
stu = Student('Pfolg', 18)
# 调用 打点调用
print(stu.name, stu.age)
# 类属性，直接打点调用
print(Student.school)

# 10.51
# 实例方法，使用对象名进行打点调用

print('{0:->20}'.format('Python'))
stu.show()

# 类方法，@classmethod修饰的方法，直接打点调用
print('\n类方法')
Student.cm()

# 静态方法，@staticmethod修饰的方法，直接打点调用
print('\n静态方法')
Student.su()

##
