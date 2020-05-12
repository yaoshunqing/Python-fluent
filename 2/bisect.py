# encoding= utf-8  
# @Time : 2020/5/12 14:47 
# @Author : Yao
# @File : bisect.py 
# @Software: PyCharm
import bisect
import sys
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' %n for n in HAYSTACK))
    demo(bisect_fn)


#根据分数对应成绩
def grade(score, break_points=[60, 70 ,80, 90], grades='FDCBA'):
    #bisect(a, x)Return the index where to insert item x in list a, assuming a is sorted.
    i = bisect.bisect(break_points, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

#用bisect.insort插入新元素
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' %new_item, my_list)
