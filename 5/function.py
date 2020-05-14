# encoding= utf-8  
# @Time : 2020/5/14 18:55 
# @Author : Yao
# @File : function.py 
# @Software: PyCharm

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print(type(factorial))