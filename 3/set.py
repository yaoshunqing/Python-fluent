# encoding= utf-8  
# @Time : 2020/5/13 14:17 
# @Author : Yao
# @File : set.py 
# @Software: PyCharm

#^表示xor，返回两个set中不相同的值
a = {1, 2, 3}
b = {4, 2, 3}
print(a ^ b)

#将元组存为字典
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
d1 = dict(DIAL_CODES)
print(d1)
d2 = dict(DIAL_CODES)
print(d2)
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
print(d3)





