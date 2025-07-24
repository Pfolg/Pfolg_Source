# 目录与文件的操作，视操作系统而定
'''
getcwd()         获取当前工作路径
listdir(path)    获取path路径下的文件和目录信息，若没有指定path，则获取当前
mkdir(path)      在指定路径下创建文件夹
makedirs()       创建多级目录
rmdir(path)
removedirs(path)
chdir(path)
walk(path)
remove(path)
rename(old,new)
stat(path)
startfile(path)
'''
import os

print('当前工作路径：', os.getcwd())
list1 = os.listdir()
print('当前路径的文件和目录信息：', list1)
print('指定目录下文件和目录信息：', os.listdir("D:\\WorkSpace"))
# 创建目录
try:
    os.mkdir('这个是用来测试os的目录')  # 二次运行报错，因为文件存在
    os.makedirs('.\\这个是用来测试os的目录\\1\\2')
except FileExistsError:
    print('FileExistsError，文件已存在')  # 于是我加了一个try
# 删除目录
try:
    os.rmdir('.\\这个是用来测试os的目录\\1\\2')  # 如果要删除的文件不存在，程序会报错
    os.removedirs('.\\这个是用来测试os的目录\\1\\2')
except FileNotFoundError:
    # os.makedirs('.\\这个是用来测试os的目录\\1\\2')
    print('FileNotFoundError 找不到文件')

# 切换工作路径
os.chdir('D:\\Pyworking\\play_games')
print('当前工作路径：', os.getcwd())
os.chdir('D:\\Pyworking\\Normal')  # 切回来

print('-' * 50, '\n')
# 遍历目录树  相当于递归操作
for dirs, dirlist, filelist in os.walk('D:\\Pyworking\\关键词分析'):
    print(dirs, '>>>', dirlist, '>>>', filelist)
#############################################################
