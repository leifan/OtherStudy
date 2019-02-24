#!/usr/bin/env python
# -*- coding:utf-8 -*- 


import win32con
import win32gui
import time

# 以qq为例子
qqWin = win32gui.FindWindow("TXGuifoundation", "QQ")  # 接收两个参数，一个是程序的类，一个是标题.目的是找到窗体



while True:
    # 然后让窗体显示出来
    win32gui.ShowWindow(qqWin, win32con.SW_SHOW)

    time.sleep(2)

    # 也可以让窗体消失
    win32gui.ShowWindow(qqWin, win32con.SW_HIDE)

    time.sleep(2)