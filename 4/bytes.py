# encoding= utf-8  
# @Time : 2020/5/14 14:16 
# @Author : Yao
# @File : bytes.py 
# @Software: PyCharm
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)

print(octets)