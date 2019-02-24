#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from PIL import ImageGrab
import win32con
import win32gui
import time
import win32api

# 以qq为例子 "TXGuifoundation"
qqWin = win32gui.FindWindow(None, "QQ")  # 接收两个参数，一个是程序的类，一个是标题.目的是找到窗体

# 然后让窗体显示出来
win32gui.ShowWindow(qqWin, win32con.SW_SHOW)

time.sleep(2)


dlg = win32gui.FindWindowEx(qqWin, None, 'Edit', None)#获取hld下第一个为edit控件的句柄

buffer = '0' *50

len = win32gui.SendMessage(dlg, win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度

win32gui.SendMessage(dlg, win32con.WM_GETTEXT, len, buffer) #读取文本
print('eeee')
print(buffer[:len-1])

#获取显示器屏幕大小
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
print(width,height)

# 也可以让窗体消失
# win32gui.ShowWindow(qqWin, win32con.SW_HIDE)
# time.sleep(2)
 
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
        
win32gui.EnumWindows(get_all_hwnd, 0)
 
for h,t in hwnd_title.items():
    if t is not "":
        print(h, t)

# python 获取窗体控件值
# spy++可以获取控件ID 我这里是0x3F8
# qqWin是母窗体句柄

# E_Ssymbol = win32gui.GetDlgItem(qqWin, 0x3F8)
 
# buff =ctypes.create_unicode_buffer(64)
# win32gui.SendMessage(E_Ssymbol, win32con.WM_GETTEXT, 32, buff)
# print (buff.value)

'''
# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (0, 0, 1160, 1080)
im = ImageGrab.grab(bbox)

# 参数 保存截图文件的路径
im.save('as.png')
'''
