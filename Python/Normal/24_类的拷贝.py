class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()
disk = Disk()

com = Computer(cpu, disk)

# 类对象的赋值，不产生新的对象
com1 = com
print(com, '子对象的内存地址：', com.cpu, com.disk)
print(com1, '子对象的内存地址：', com1.cpu, com1.disk)

# 类对象的浅拷贝
import copy

com2 = copy.copy(com)
print('-' * 50)
print(com, '子对象的内存地址:', com.cpu, com.disk, f'\n{'-' * 50}\n', com2, '子对象的内存地址:', com2.cpu, com2.disk)
# 只是产生了一个新的com2对象，cpu和disk内存地址不变

# 类对象的深拷贝
com3 = copy.deepcopy(com)
print('-' * 50)
print(com, '子对象的内存地址:', com.cpu, com.disk, f'\n{'-' * 50}\n', com3, '子对象的内存地址:', com3.cpu, com3.disk)
# 对象和子对象都会重新产生，即内存地址改变
