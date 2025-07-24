# -*- coding: utf-8 -*-
# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 45.1_UDP的发送方    ||    Author >>> Pfolg
# Date >>> 2024/6/9 and Time >>> 10:24
# 接收方先开启
from socket import socket, AF_INET, SOCK_DGRAM

send_socket = socket(AF_INET, SOCK_DGRAM)

data = input('请输入数据:')
# 指定接收方的ip和端口
ip_port = ('172.27.96.1', 8888)

# send
send_socket.sendto(data.encode('utf-8'), ip_port)

# 接收回复
recv, add = send_socket.recvfrom(1024)
print('接收:', recv.decode('utf-8'))

send_socket.close()
