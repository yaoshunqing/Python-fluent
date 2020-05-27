# encoding= utf-8  
# @Time : 2020/5/27 7:41 
# @Author : Yao
# @File : is.py 
# @Software: PyCharm

charles = {'name':'Charles', 'born': 1832}
lewis = charles
alex = {'name':'Charles', 'born': 1832}
#==比较两个对象的值，而is比较两个对象的标识
print(lewis is charles, lewis == charles, alex is charles, alex == charles)

#浅复制列表
l1 = [1]
l2 = [1] #相同赋值
l3 = list(l1) #浅复制，也可以使用l3 = l1[:]替代
l4 = l1 #相同引用，修改一者另一者也变化
print(l1 == l2 == l3 == l4, l1 is l4, l1 is l3)

#但是在为包含可变元素的内容进行浅复制就会出现问题
l1 = [3, [66,44], (7,8)]
l2 = l1[:]
l1.remove(3)
l2[1] += [33,22]
l2[2] += (10,11)
#列表是相同引用，而元组则成了新建元组
print('l1',l1)
print('l2',l2)

#深复制副本不共享内部对象的引用
#一浅一深
from copy import deepcopy,copy
l1 = [3, [66,44], (7,8)]
l2 = deepcopy(l1)
l2[1] += [33,22]
l2[2] += (10,11)
print('l1',l1)
print('l2',l2)

