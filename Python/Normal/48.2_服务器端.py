# -*- coding: utf-8 -*-
# Project >>> Pfolg   ||    Environment >>> PyCharm
# FileName >>> 48.2_服务器端    ||    Author >>> Pfolg
# Date >>> 2024/6/11 and Time >>> 15:31
import threading
from socket import socket, AF_INET, SOCK_STREAM
import wx


class Pfolgsever(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=2, title='Pflog', pos=wx.DefaultPosition, size=(400, 450))
        # 窗口放一个面板
        pl = wx.Panel(self)
        # 面板上放一个盒子
        box = wx.BoxSizer(wx.VERTICAL)  # 垂直方向上自动排版
        # 可伸缩的网格布局
        win1 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向上布局

        start_sever_btu = wx.Button(pl, size=(133, 40), label='启动服务')
        record_sever_btu = wx.Button(pl, size=(133, 40), label='保存聊天记录')
        stop_sever_btu = wx.Button(pl, size=(133, 40), label='停止服务')

        # 放到可伸缩布局中
        win1.Add(start_sever_btu, 1, wx.TOP)
        win1.Add(record_sever_btu, 1, wx.TOP)
        win1.Add(stop_sever_btu, 1, wx.TOP)

        # 将可伸缩的网格布局放到box中
        box.Add(win1, 1, wx.ALIGN_CENTRE)

        # 只读的多行文本框
        self.show_txt = wx.TextCtrl(pl, size=(400, 410), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_txt, 1, wx.ALIGN_CENTRE)

        pl.SetSizer(box)
        ### 以上为界面绘制，以下为功能
        self.isOn = False  # 服务器的启动状态，默认False，没有启动
        # 服务器IP和端口
        self.host_port = ('', 8888)  # 空字符串——本机的所有IP
        # socket
        self.sever_socket = socket(AF_INET, SOCK_STREAM)

        self.sever_socket.bind(self.host_port)

        self.sever_socket.listen(5)

        # 创建字典存储
        self.session_thread_dic = {}  # key=value{客户端的名称key：会话线程value}

        # 当鼠标点击按钮进行操作
        self.Bind(wx.EVT_BUTTON, self.start_sever, start_sever_btu)

    def start_sever(self, event):
        # 判断服务器是否启动
        if not self.isOn:
            # 启动服务器
            self.isOn = True
            # 创建主线程对象
            main_thread = threading.Thread(target=self.do_work)
            # 设置为守护线程，父线程执行结束（窗体界面），子线程也自动关闭
            main_thread.daemon = True
            # 启动主线程
            main_thread.start()

    def do_work(self):
        # 判断isOn
        while self.isOn:
            # 接收客户端的连接请求
            client, add = self.sever_socket.accept()
            user_name = client.recv(1024).decode('utf-8')
            # 创建一个会话线程
            sesstion_thread = SesstionThread(client, user_name, self)
            self.session_thread_dic[user_name] = sesstion_thread

            # 启动会话线程
            sesstion_thread.start()
        # isOn==False时执行
        self.sever_socket.close()


class SesstionThread(threading.Thread):
    def __init__(self, client_socket, user_name, server):
        pass

    def run(self) -> None:
        pass


if __name__ == '__main__':
    # 初始化APP
    app = wx.App()
    sever = Pfolgsever()
    sever.Show()  # Win(('Pfolg').show)

    # 循环刷新显示
    app.MainLoop()
