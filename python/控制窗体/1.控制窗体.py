#!/usr/bin/env python
# -*- coding:utf-8 -*- 


import win32con
import win32gui
import win32api
import time

# 以qq为例子
qqWin = win32gui.FindWindow("TXGuifoundation", "QQ")  # 接收两个参数，一个是程序的类，一个是标题.目的是找到窗体
print(qqWin)

# 获得窗口的菜单句柄
menuHandle = win32gui.GetMenu(qqWin)
print(menuHandle)
# 获得子菜单或下拉菜单句柄   
# 参数：菜单句柄 子菜单索引号
subMenuHandle = win32gui.GetSubMenu(menuHandle, 0)
print(subMenuHandle)

# # 搜索子窗口
# # 枚举子窗口
# hwndChildList = []     
# win32gui.EnumChildWindows(qqWin, lambda hwnd, param: param.append(hwnd),  hwndChildList)
# print(hwndChildList)

while True:
    # # 然后让窗体显示出来
    # win32gui.ShowWindow(qqWin, win32con.SW_SHOW)

    # time.sleep(2)

    # # 也可以让窗体消失
    # win32gui.ShowWindow(qqWin, win32con.SW_HIDE)

    time.sleep(3)
    print(win32api.GetCursorPos())
    # 通过坐标获取窗口句柄
    # hw = win32api.WindowFromPoint(win32api.GetCursorPos())
    # print(hw)
    # print(win32gui.GetClassName(hw))
    # print(win32gui.GetWindowText(hw))
    # print(win32gui.GetwindowRect(hw))