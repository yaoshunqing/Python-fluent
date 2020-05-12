# encoding= utf-8  
# @Time : 2020/5/12 15:58 
# @Author : Yao
# @File : deque.py 
# @Software: PyCharm
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
#队列往后循环移动
dq.rotate(3)
print(dq)
#队列往前循环移动
dq.rotate(-3)
print(dq)
#队列添加一个值或多个值,由于最大长度限制，会在相反方向删去数据
dq.appendleft(-1)
print(dq)
dq.extend([11, 12])
print(dq)
#先进先出
dq.popleft()
print(dq)