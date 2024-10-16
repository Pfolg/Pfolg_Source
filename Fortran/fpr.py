import os
import time

# os.system("cls")  # 开局清屏
file=input("NAME=")
print("构建术式……")

os.system(f"gfortran -Wall {file}")
print("构建完成！")
time.sleep(2)
print("发动术式！（脑补一段精彩的高度玄幻的画面……）\n")
os.system(r".\a")
time.sleep(1)
try:
    os.remove(".\\a.exe")
    print("\n已修复术式产生的影响！")
except FileNotFoundError:
    print("\n啊咧，好像出现了问题？")
    
input("回车离开魔法阵……")
