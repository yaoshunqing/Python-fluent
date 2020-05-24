# encoding= utf-8  
# @Time : 2020/5/22 14:49 
# @Author : Yao
# @File : bobo.py 
# @Software: PyCharm
# import bobo
#
# @bobo.query('/')
# def hello(person):
#     return 'Hello%s!' % person


from functools import reduce
from operator import mul
n = 5
#使用map需要两个迭代数组并且不是函数阶乘运算
a = map(lambda a, b:a*b, range(1, n+1),range(1, n+1))
print([i for i in a])
#reduece则是阶乘迭代
a = reduce(lambda a, b:a*b, range(1, n+1))
print(a)
#使用mul替代乘法匿名函数
a = reduce(mul, range(1, n+1))
print(a)

from operator import methodcaller
#methodcaller实现迭代函数调用
s = 'hello'
upcase = methodcaller('upper')
print(upcase(s))
hip = methodcaller('replace', 'l', 'a')
print(hip(s))

#冻结函数中某个参数
from functools import partial
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(5))))




