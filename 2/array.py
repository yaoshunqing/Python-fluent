# encoding= utf-8  
# @Time : 2020/5/12 15:32 
# @Author : Yao
# @File : array.py 
# @Software: PyCharm

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
floats2 = array('d')
#注意这里读和写是有差别的！
with open('nums.bin', 'wb+') as f:
    floats.tofile(f)
with open('nums.bin', 'rb+') as f:
    floats2.fromfile(f, 10**7)
print(floats == floats2)
