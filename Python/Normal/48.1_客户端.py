# -*- coding: utf-8 -*-
# Project >>> Pfolg   ||    Environment >>> PyCharm
# FileName >>> 48_客户端    ||    Author >>> Pfolg
# Date >>> 2024/6/11 and Time >>> 14:49
import wx


class Win(wx.Frame):
    def __init__(self, client_name):
        # 调用父类的初始化方法
        wx.Frame.__init__(self, None, id=1, title=client_name + '的客户端界面',
                          pos=wx.DefaultPosition, size=(400, 450))  # 400宽，450高
        # 创建面板对象
        pl = wx.Panel(self)
        # 在面板中放上盒子
        box = wx.BoxSizer(wx.VERTICAL)  # 垂直方向布局
        # 可伸缩的网格布局
        fgz1 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局
        # 创建两个按钮
        conn_btn = wx.Button(pl, size=(200, 40), label='连接')
        coon_btn = wx.Button(pl, size=(200, 40), label='断开')

        # 把两个按钮放到可伸缩的网格布局中
        fgz1.Add(conn_btn, 1, wx.TOP | wx.LEFT)
        fgz1.Add(coon_btn, 1, wx.TOP | wx.RIGHT)
        # 添加到可伸缩的网格布局中
        box.Add(fgz1, 1, wx.ALIGN_CENTRE)

        # 只读文本框
        self.show_txt = wx.TextCtrl(pl, size=(400, 210), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_txt, 1, wx.ALIGN_CENTRE)

        # 创建聊天框内容聊天框
        self.chat_txt = wx.TextCtrl(pl, size=(400, 120), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.chat_txt, 1, wx.ALIGN_CENTRE)
        # 可伸缩的网格布局
        fgz2 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局
        # 创建两个按钮
        reset_btn = wx.Button(pl, size=(200, 40), label='重置')
        send_btn = wx.Button(pl, size=(200, 40), label='发送')
        fgz2.Add(reset_btn, 1, wx.TOP | wx.LEFT)
        fgz2.Add(send_btn, 1, wx.TOP | wx.RIGHT)

        box.Add(fgz2, 1, wx.ALIGN_CENTRE)

        # 将盒子放到面板中
        pl.SetSizer(box)


if __name__ == '__main__':
    # 初始化APP
    app = wx.App()
    client = Win('Pfolg')
    client.Show()  # Win(('Pfolg').show)

    # 循环刷新显示
    app.MainLoop()
