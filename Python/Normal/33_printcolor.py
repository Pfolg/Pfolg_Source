# print("\033[显示方式；前景颜色；背景颜色m…\033[0m")

"""
意义	显示方式
默认	    0
高亮显示	1
下划线	4
闪烁	    5
反白显示	7
不可见	8
"""
'''
颜色	    前景色	背景色
黑色	    30	    40
红色	    31  	41
绿色	    32	    42
黄色	    33	    43
蓝色	    34  	44
紫红色	35	    45
青蓝色	36  	46
白色  	37	    47
没有设置的话就是默认
'''
# RGB
print('\033[38;2;255;0;0m' + '红色文本' + '\033[0m')
print('\033[38;2;0;255;0m' + '绿色文本' + '\033[0m')
print('\033[38;2;0;0;255m' + '蓝色文本' + '\033[0m')

print('\033[31m' + '红色文本' + '\033[0m')
print('\033[32m' + '绿色文本' + '\033[0m')
print('\033[33m' + '黄色文本' + '\033[0m')
print('\033[34m' + '蓝色文本' + '\033[0m')
print('\033[35m' + '洋红色文本' + '\033[0m')
print('\033[36m' + '青色文本' + '\033[0m')
print('\033[37m' + '白色文本' + '\033[0m')

# for i in range(100):
#     print('\033[38;2;255;0;0m' + ' WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by \'ReadTimeoutError("HTTPSConnectionPool(host=\'pypi.tuna.tsinghua.edu.cn\', port=443): Read timed out.' + '\033[0m')
