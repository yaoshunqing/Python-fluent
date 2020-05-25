# encoding= utf-8  
# @Time : 2020/5/25 15:02 
# @Author : Yao
# @File : fibonacci.py 
# @Software: PyCharm
import functools
from clock import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(5))

#使用lru_cache改善缓存性能
@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
print(fibonacci(5))