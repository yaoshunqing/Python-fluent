# encoding= utf-8  
# @Time : 2020/5/29 9:33 
# @Author : Yao
# @File : vector2d_v0.py 
# @Software: PyCharm

from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def __iter__(self):
        #return (i for i in (self.x, self.y))
        yield self.x
        yield self.y

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({}, {})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)



v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1))
#注意repr与str的区别，没有str时会调用repr
print('%r' %v1)
print('%s' %v1)
print(format(v1, '.2f'))
print(hash(v1), hash(v2))
print(set([v1, v2]))

print(bytes(v2))
v2_clone = Vector2d.frombytes(bytes(v2))
print(v2_clone)


