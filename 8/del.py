# encoding= utf-8  
# @Time : 2020/5/27 8:47 
# @Author : Yao
# @File : del.py 
# @Software: PyCharm

import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print("Gone with the wind.")
#list和dict不能直接作为弱引用对象，因此用集合set
ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
#将s2指向另一个值,s1失去最后的引用，被垃圾回收
s2 = 'spam'

l1 = [1]
l2 = []
l3 = l1
l4 = l1[:]
l5 = []
l2[:] = l1
l5[:] = l1[:]

print(l1, l2, l3, l4, l5 ,sep=' ')
#只有l3是l1的引用，两者一致。其余的都是复制
print(l1 is l2, l1 is l3, l1 is l4, l1 is l5)

