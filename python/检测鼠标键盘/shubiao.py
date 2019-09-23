
import os
from PIL import ImageGrab
from PIL import Image
import time
import datetime

from pynput import keyboard,mouse

pointXY = [0,0,0,0]
pointXY_tmp = [0,0]

def saveImg(x_s,y_s,x_e,y_e):
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    bbox = (x_s,y_s,x_e,y_e)
    im = ImageGrab.grab(bbox)
    # 参数 保存截图文件的路径
    signtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[0:17]
    #time.strftime("%Y%m%d%H%M%S", time.localtime())

    pathimgname = os.getcwd() + '\\output\\' + str(signtime + '.png')
    im.save(pathimgname)
    print('save img:', pathimgname)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.alt_l:
        pointXY[0:2] = pointXY_tmp[0:2]
        print('pointXY:',pointXY)
    if key == keyboard.Key.alt_r:
        pointXY[2:4] = pointXY_tmp[0:2]
        print('pointXY:',pointXY)
        saveImg(pointXY[0],pointXY[1],pointXY[2],pointXY[3])
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    pointXY_tmp[0] = x
    pointXY_tmp[1] = y
    print('pointXY_tmp:',pointXY_tmp)

    

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up', 
        (x, y)))

# Collect events until released

keyboard_listener=keyboard.Listener(on_press=on_press,on_release=on_release)
mouse_listener=mouse.Listener(on_click=on_click,on_move=on_move,on_scroll=on_scroll)
lst=[keyboard_listener,mouse_listener]

for t in lst:
    t.start()

for t in lst:
    t.join()
