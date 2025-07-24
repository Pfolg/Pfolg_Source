# -*- coding: utf-8 -*-
# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 46_模拟客服    ||    Author >>> Pfolg
# Date >>> 2024/6/9 and Time >>> 10:39
from socket import socket, AF_INET, SOCK_DGRAM

recv_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定
recv_socket.bind(('172.27.96.1', 8888))
print('服务器已上线!正在监听信息......')
while True:
    re_data, add = recv_socket.recvfrom(1024)
    if re_data == 'exit':
        break
    print('收到:', re_data.decode('utf-8'))
    data = input('回复:')
    recv_socket.sendto(data.encode('utf-8'), add)
    if data == 'exit':
        break

recv_socket.close()
