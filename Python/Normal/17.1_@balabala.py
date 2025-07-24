##
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender  # 私有的实例属性

    #  使用@property装饰器 修改方法，将方法转为属性使用
    @property  # 方法当属性用，只能查看，不能修改
    def gender(self):
        return self.__gender

    # 将gender属性设置为可写属性
    @gender.setter
    def gender(self, value):
        if value != 'male' and value != 'female':
            print('Gendererror!Gender=male')
            self.__gender = 'male'
        else:
            self.__gender = value


stu = Student('Pfolg', 'male')
print(f'00001  {stu.name}\'s gender is {stu.gender}')

# 尝试修改属性值
# stu.gender = 'male'  # AttributeError: property 'gender' of 'Student' object has no setter
stu.gender = 'female'
print(stu.gender)
print(f'00002  {stu.name}\'s gender is {stu.gender}')
##
