# encoding= utf-8  
# @Time : 2020/5/11 9:25 
# @Author : Yao
# @File : vector.py 
# @Software: PyCharm
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #字符串表达式
    def __repr__(self):
        return  'Vector(%r, %r)' %(self.x,self.y)

    def __abs__(self):
        #hypot平方根函数
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)