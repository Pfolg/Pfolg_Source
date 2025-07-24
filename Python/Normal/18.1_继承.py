##
class Person:  # 默认继承object
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f'Hello,everybody!\nMy name is {self.name}. I am a {self.age}-year-old {self.gender}')


# Student继承Person类
class Student(Person):
    def __init__(self, name, age, student_number, gender):
        # 调用父类的初始化方法，为name和age赋值
        super().__init__(name, age, gender)
        self.student_number = student_number


class Doctor(Person):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)
        self.department = department


# 创建一个子类对象
stu = Student('Daming', 18, '123456789', 'male')
stu.show()

doc = Doctor('Fojiang', 50, 'FB1', 'male')
doc.show()
##
