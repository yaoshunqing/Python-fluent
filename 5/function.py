# encoding= utf-8  
# @Time : 2020/5/14 18:55 
# @Author : Yao
# @File : function.py 
# @Software: PyCharm

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

print(type(factorial))

def reverse(word):
    return word[::-1]

print(reverse('Hello'))

print(list(map(factorial, range(6))))
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
#使用列表推导替换map或filter
print([factorial(n) for n in range(6)])
print([factorial(n) for n in range(6) if n % 2 ])


