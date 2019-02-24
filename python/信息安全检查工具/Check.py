# -*- coding:utf-8 -*- 

'''
功能：
打开需要坚持的安全工具，截图保存记录
安全检查项11：
1.安全桌面
2.屏蔽设置
3.磁盘共享查询
4.
'''
import os
import time
import win32con
import win32gui
import win32api
from PIL import ImageGrab

user = 'lwx531911'

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (0, 0, 1160, 1080)
# im = ImageGrab.grab(bbox)

# 参数 保存截图文件的路径
#im.save(user + '.png')

import winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, \
                 r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
cwd= winreg.QueryValueEx(key, "Desktop")[0]

print(cwd)

def runApp():
    #os.system(u"C:\\Windows\\System32\\notepad.exe")

    #非阻塞运行
    # 最后一个参数表示是窗口属性，0表示不显示，1表示正常显示，2表示最小化，3表示最大化
    res = win32api.ShellExecute(0, 'open', 'C:\\Windows\\System32\\notepad.exe', '', '', 3)
 
runApp()




