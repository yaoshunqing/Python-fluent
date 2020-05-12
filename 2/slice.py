# encoding= utf-8  
# @Time : 2020/5/12 13:33 
# @Author : Yao
# @File : slice.py 
# @Software: PyCharm

l = [10, 20, 30, 40, 50, 60]

print(l[:2])
print(l[2:])
print(l[:3])
print(l[1:6:2]) #每两个取值
#负数代表反向取值
print(l[::-2])
print(l[::3])

#使用切片进行修改删除等操作
l[2:5] = [0, 0, 0]
print(l)
del l[2:5]
print(l)

l = [1, 2, 3]
#复制序列
print(l * 5)

#建立由列表组成的列表
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

#错误建立法,三个列表是指向同一个列表的引用，一旦修改全部都会变化
wrong_board = [['_'] * 3] * 3
print(wrong_board)
wrong_board[1][2] = 'X'
print(wrong_board)

