##
class Person:  # 默认继承object
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f'Hello,everybody!\nMy name is {self.name}. I am a {self.age}-year-old {self.gender}')
        pass


# Student继承Person类
class Student(Person):
    def __init__(self, name, age, student_number, gender):
        # 调用父类的初始化方法，为name和age赋值
        super().__init__(name, age, gender)
        self.student_number = student_number

    def show(self):
        # super().show()  # 调用父类方法
        print(f'子类1  Hello,everybody!\nMy name is {self.name}. I am a {self.age}-year-old {self.gender},my student number is {self.student_number} ')


class Doctor(Person):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)
        self.department = department

    def show(self):
        # super().show()  # 调用父类方法
        print(f'子类2  Hello,everybody!\nMy name is {self.name}. I am a {self.age} {self.gender},I am from {self.department}')


# 创建一个子类对象
stu = Student('Daming', 18, '123456789', 'boy')
stu.show()  # 调用子类自己的方法

doc = Doctor('Fojiang', 50, 'man', 'FB1')
doc.show()

##
