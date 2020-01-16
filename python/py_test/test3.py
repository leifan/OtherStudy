

import os

def my_max(x, y):
    '''
    求两数最大值

    my_max(x, y)
        返回x,y中最大值
    '''
    z = x if x >y else y
    return z

help(my_max)
print('*'*50)
print(my_max.__doc__)