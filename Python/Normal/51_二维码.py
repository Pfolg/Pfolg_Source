# -*- coding: utf-8 -*-
# Project >>> make_pie.py   ||    Environment >>> PyCharm
# FileName >>> 51_二维码    ||    Author >>> Pfolg
# Date >>> 2024/6/15 and Time >>> 22:35
"""
create(url):创建二维码

png(path):将二维码保存为png

svg(path):将二维码保存为svg

terminal():获取二维码输出到终端
"""
import time

import pyqrcode

# 设置二维码信息
s = "https://www.baidu.com"

# 生成二维码
url = pyqrcode.create(s)
print(type(url))
# 保存二维码
url.png("baidu.png", scale=8)
# 打印二维码
# print(url.terminal(quiet_zone=1))
time.sleep(2)
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

barcode_url = ''
barcodes = decode(Image.open('./baidu.png'))
for barcode in barcodes:
    barcode_url = barcode.data.decode("utf-8")
print(barcode_url)

qr = qrcode.QRCode()
qr.add_data(barcode_url)
#invert=True白底黑块,有些app不识别黑底白块.
qr.print_ascii(invert=True)
