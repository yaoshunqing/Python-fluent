# encoding= utf-8  
# @Time : 2020/6/1 15:00 
# @Author : Yao
# @File : reduce.py 
# @Software: PyCharm
from functools import reduce
from operator import xor

#求整数0~5的累计异或的三种方式
n = 0
for i in range(6):
    n ^= i
print(n)
print(reduce(lambda a, b: a ^ b, range(6)))
print(reduce(xor, range(6)))



