# -*- coding: utf-8 -*-
# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 44.1_服务器多次通信    ||    Author >>> Pfolg
# Date >>> 2024/6/8 and Time >>> 21:57
import socket

# 创建对象
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定
socket_object.bind(('192.168.200.1', 8888))  # 这里是元组

# 监听量
socket_object.listen(5)
print('服务器已启动')
# 等待连接
client, address = socket_object.accept()

# 接收数据
info = client.recv(1024).decode('utf-8')
while info != 'exit':
    print('接收:', info)
    # 准备发送的数据
    data = input('发送:')

    # 回复客户端
    client.send(data.encode('utf-8'))
    if data == 'exit':
        break
    print('已发送，等待对方回复......')
    info = client.recv(1024).decode('utf-8')  # 改变变量

client.close()
socket_object.close()