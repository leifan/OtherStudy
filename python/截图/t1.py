# -*- coding: UTF-8 -*-

import os
from PIL import ImageGrab
from PIL import Image

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (0, 0, 500, 500)
im = ImageGrab.grab(bbox)
# 参数 保存截图文件的路径
im.save('1.jpeg')

bbox = (500, 500, 1000, 1000)
im = ImageGrab.grab(bbox)
# 参数 保存截图文件的路径
im.save('2.jpeg')

#图片压缩后的大小
width_i = 1000
height_i = 1000

#每行每列显示图片数量
line_max = 3
row_max = 3

#参数初始化
all_path = []
num = 0
pic_max=line_max*row_max

dirName = os.getcwd()

for root, dirs, files in os.walk(dirName):
        for file in files:
            if "jpeg" in file:
                    all_path.append(os.path.join(root, file))

toImage = Image.new('RGBA',(width_i*line_max,height_i*row_max))


for i in range(0,row_max): 
    for j in range(0,line_max):
        pic_fole_head =  Image.open(all_path[num])
        width,height =  pic_fole_head.size
        print(i,j,width,height)
    
        tmppic = pic_fole_head.resize((width_i,height_i))
        print(tmppic)
        loc = (int((i%line_max)*width_i),int((j%line_max)*height_i))
        print("第" + str(num) + "存放位置" + str(loc))
        toImage.paste(tmppic,loc)
        num= num + 1

        if num >= len(all_path):
                print(num, " break")
                break

    if num >= pic_max or num >= len(all_path):
        print(num, "-- break")
        break


print(toImage.size)
toImage.save('merged.png')
