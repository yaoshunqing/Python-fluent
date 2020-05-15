# encoding= utf-8  
# @Time : 2020/5/15 10:09 
# @Author : Yao
# @File : lambda.py 
# @Software: PyCharm

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda x:x[::-1]))
print(sorted(fruits, key=lambda x:x[:-1]))
l = lambda x:x[::-1]
print(l('hello'))
print((lambda x:x[::-1])('hello')) #olleh

l1 = lambda x:x[::2] #每隔两个切片
print(l1('hello')) #hell

