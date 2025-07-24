# 记不住来查
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建对象
a = A()
b = B()
c = C('张三', 18)

print('-'*50)
print('对象a的属性字典：',a.__dict__)
print('对象b的属性字典：',b.__dict__)
print('对象c的属性字典：',c.__dict__)

print('-'*50)
print('对象a所属的类：',a.__class__)
print('对象b所属的类：',b.__class__)
print('对象c所属的类：',c.__class__)

print('-'*50)
print('A类的父类元组:',A.__bases__)
print('B类的父类元组:',B.__bases__)
print('C类的父类元组:',C.__bases__)  # 没有爷爷类

print('-'*50)
print('A类的父类：',A.__base__)
print('B类的父类：',B.__base__)
print('C类的父类：',C.__base__)  # 只显示第一个父类

print('-'*50)
print('A的层次结构：',A.__mro__)
print('B的层次结构：',B.__mro__)
print('C的层次结构：',C.__mro__)  # 首先继承+间接继承

print('-'*50)  # 方法
print('A类的子类列表：',A.__subclasses__())
print('B类的子类列表：',B.__subclasses__())
print('C类的子类列表：',C.__subclasses__())