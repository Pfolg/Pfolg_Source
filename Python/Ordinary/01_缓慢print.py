# -*- coding: utf-8 -*-
# Project >>> make_files.py   ||    Environment >>> PyCharm
# FileName >>> 缓慢print    ||    Author >>> Pfolg
# Date >>> 2024/6/30 and Time >>> 10:05
import time

text = ('这个示例非常基础，没有持久化存储功能，所以关闭程序后数据会丢失。为了持久化存储，你可以将待办事项保存到文件（如JSON或CSV'
        '格式）中，并在程序启动时读取这些文件。为了提高用户体验，可以添加更多的功能，比如编辑待办事项、设置提醒等。这个简单的待办事项列表应用可以作为学习Python '
        'GUI编程的起点。随着你技能的提升，你可以添加更多的功能和改进用户界面，使其更加完善和实用。')
i = 0
while i != len(text)+1:
    print(f'\r{text[0:i]}', end='')
    i += 1
    time.sleep(0.1)
