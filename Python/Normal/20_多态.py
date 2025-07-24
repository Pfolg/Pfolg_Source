class Person:
    def eat(self):
        print('吃葡萄不吐葡萄皮')


class Cat:
    def eat(self):
        print('猫猫猫猫')


class Dog:
    def eat(self):
        print('劳资最喜欢狗嘞！')


'''三类独立，都有一个同名方法'''


# 编函数
def fun(mnu):
    mnu.eat()  # 可通过该对象调用eat方法


per = Person()
cat = Cat()
dog = Dog()

# 调用fun函数   Python中的多态，不关心数据类型，只关心对象是否具有同名方法
fun(per)
fun(cat)
fun(dog)

'''
吃葡萄不吐葡萄皮
猫猫猫猫
劳资最喜欢狗嘞！
'''
