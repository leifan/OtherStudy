#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
'''
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

print(para_str)

#测试2
var1 = 100
if var1:
  print ("1 - if 表达式条件为 true")
  print (var1)

  var2 = 1
if var2:
    print ("2 - if 表达式条件为 true")
    print (var2)
print ("Good bye!")


import hello
import sys

print(sys.path)

hello.helloworld("nnnnmmm")

#输入测试
str = input("please input:")
print("you str:",str)
'''
"""
#文件写操作测试
f = open("hello.py","w")
f.write("#我是测试写入文本\n")
f.write("#helloworld.py模块\n")
str = '''
def helloworld(str):
	print("helloworld ",str)
	return 
'''
f.write(str)
str = '''
def hellotest(str):
	print("hellotest ",str)
	return 
'''
f.write(str)
f.close()
#测试写一个模块，然后再调用
from hello import *
helloworld("leifan test")
hellotest("leifan test")
 

 
f = open("hello.py","r")
str = f.read()
print(str)
f.close()
"""

'''
#!/usr/bin/python3
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
'''
'''
#!/usr/bin/python3
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

'''
'''
import os
print(os.getcwd())
#os.system("calc")

'''



import glob

print(glob.glob('*.py'))
























































