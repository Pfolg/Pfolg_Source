class FatherA:
    def __init__(self, name):
        self.name = name

    def showA(self):
        print('A中的方法')


class FatherB:
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('B中的方法')


class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):
        # 需要调用两个父类的方法，使用父类名称区别
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)
        self.gender = gender


son = Son('张三', 20, '男')
son.showA()
son.showB()
print(son.name, son.age, son.gender)
print('一个父类也可以拥有无数多个子类')