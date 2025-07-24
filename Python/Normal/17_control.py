##
class Student:
    # 双下划线
    def __init__(self, age, name, gender):
        self._name = name  # 受保护的，只能本类和子类访问
        self.__age = age  # 表示私有，只能类本身去访问
        self.gender = gender  # 普通的实例属性，随便用

    def _fun1(self):
        print('受保护的，子类及本身可访问')

    def __fun2(self):
        print('私有的，只有定义的类可访问')

    def fun3(self):  # 普通的实例方法
        self._fun1()  # 类本身访问受保护的方法
        self.__fun2()  # 类本身访问私有方法
        print(self._name)  # 受保护的属性
        print(self.__age)  # 私有的实例属性


# 创建一个student对象
stu = Student(50, 'QQ', 'unkoown')
# 目前处于类的外部
print(stu._name)
'''
print(stu.__age)  # AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?
# 出了类的范围就不能使用了'''
stu._fun1()  # 访问受保护的
# stu.__fun2()  # 私有的  运行报错
# 访问私有：
print(stu._Student__age)

stu._Student__fun2()

print('展示stu中所有可访问的对象', dir(stu))


##
