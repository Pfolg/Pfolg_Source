# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   getInformation |User    Pfolg
# 2024/8/21   13:23
import os
import re
import sys

import requests
# import prettytable
import json
# from plyer import notification
import tkinter

try:
    with open('Information.txt', 'r') as f:
        con0 = json.load(f)
except FileNotFoundError:
    con0 = ""

url = "https://jwc.cuit.edu.cn/"

a = requests.get(url)
a.encoding = "utf-8"
b = a.text
# print(b)

c = re.findall("<H5 class=\"col_5\"><A href=\"(.*)\" target=\"_blank\" style=\"color: #ff6a6a\">(.*)</A></H5>", b)
d = re.findall("<H6 style=\"color: #ff6a6a\">(.*)</H6>", b)
# print(c, d)
e = re.findall("<H5 class=\"col_5\"><A href=\"(.*)\" target=\"_blank\">(.*)</A></H5>", b)
f = re.findall("<H6>(.*)</H6>", b)

# table = prettytable.PrettyTable()
# table.field_names = ["时间", "链接", "标题"]
# for i in range(len(c)):
#     table.add_row([d[i], f"{url}" + c[i][0], c[i][1]])

dicInf = {}
for i in range(len(c)):
    dicInf[c[i][1]] = [d[i], f"{url}" + c[i][0]]

# table.add_row(["-", "-", "-"])
#
# for k in range(len(e)):
#     table.add_row([f[k], f"{url}" + e[k][0], e[k][1]])

for j in range(len(e)):
    dicInf[e[j][1]] = [f[j], f"{url}" + e[j][0]]
# print(table)
# print("上半部分是学校标红的通知，下半部分是蓝色的通知")
# print(dicInf)
# print(json.dumps(dicInf, ensure_ascii=False, indent=4))


with open('Information.txt', 'w') as file:
    json.dump(dicInf, file, ensure_ascii=False, indent=4)

with open('Information.txt', 'r') as f:
    con1 = json.load(f)
print(json.dumps(con1, ensure_ascii=False, indent=4))

if con0 != con1:
    msg = "教务处发布了新的通知！"
else:
    msg = "教务处尚未发布新的通知！"
if con0 == "":
    sys.exit()


# notification.notify(
#     # title='提醒',
#     message=msg,
#     timeout=10,  # 通知显示时间，单位为秒
# )
def openWeb(event):
    os.system(f"start {url}")


if __name__ == '__main__':
    bg = "#000000"
    window = tkinter.Tk()
    window.overrideredirect(True)
    window.title("教务处通知监控")
    screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = int(screen_w / 7), int(screen_h / 10)
    window.geometry(f'{w}x{h}+{int(screen_w / 1.2)}+{int(screen_h / 1.25)}')
    window.resizable(False, False)
    window.config(background=bg)
    # window.iconbitmap(".\\resource\\pg.ico")
    # window.attributes('-alpha', 0.9)
    tkinter.Label(
        window, text="\n" + msg, font=("Segoe UI", 12), background=bg, foreground="#ffffff"
    ).pack()
    link = tkinter.Label(window, text="瞅一眼", cursor="hand2", background=bg, foreground="#4290ea")
    link.pack()
    link.bind("<Button-1>", openWeb)

    window.after(10000, lambda: window.destroy())
    window.mainloop()
