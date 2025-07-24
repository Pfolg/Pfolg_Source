class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.age}，今年{self.age}岁。')


person = Person('李四', 50)
print(dir(person))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__',    来自object
''' 'age', 'name', 'show']'''    # 来自我的方法

print(person)  # <__main__.Person object at 0x000001C4DA1BE690>  自动调用了__str__方法

