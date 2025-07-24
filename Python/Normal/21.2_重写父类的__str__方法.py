class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.age}，今年{self.age}岁。')

    #  重写父类方法
    def __str__(self):
        return 'This is a person with <name> and <age>两个实例属性'  # 返回值是一个str


per = Person('王五', 42)
print(per)
print(per.__str__())
