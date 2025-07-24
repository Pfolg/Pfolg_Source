# -*- coding: utf-8 -*-
# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 43.1_服务器    ||    Author >>> Pfolg
# Date >>> 2024/6/8 and Time >>> 21:21

# 服务器端一定要先启动
from socket import socket, AF_INET, SOCK_STREAM

# AF_INET 用于Internet之间的进程通信
# SOCK_STREAM 表示TCP协议编程

# 创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)

# 绑定IP地址和端口
ip = '192.168.200.1'
port = 8888
server_socket.bind((ip, port))

# 使用listen()开始监听
server_socket.listen(5)
print('服务器已启动')

# 等待客户端连接
client_socket, client_addr = server_socket.accept()

# 接收数据
data = client_socket.recv(1024)
print('客户端发来的数据为', data.decode('utf-8'))  # 解码

# 关闭
server_socket.close()
