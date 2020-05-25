# encoding= utf-8  
# @Time : 2020/5/25 10:08 
# @Author : Yao
# @File : decorate.py 
# @Software: PyCharm

def deco(func):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print('running target()')

#装饰器会替换函数
target()
print(target)

b = 6
#这样写pycharm直接提示错误，因为python会
#在编译函数体时将内部进行赋值的变量视为局部变量
#即使它为全局变量
# def f2(a):
#     print(a)
#     print(b)
#     b = 9
#因此我们要让函数内部将b视为全局变量的话这样做
def f2(a):
    global b
    print(a)
    print(b)
    b = 9

f2(3)
print(b)

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

#类名()这是初始化一个实例，之后类名()(value)才是调用
avg = Averager()
print(avg)
print(avg(10))
print(Averager()(10))

#高阶函数实现
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager
avg = make_averager()
print(avg(10))

#把变量标记为自由变量，这样就不存在会在函数中创建局部变量的问题
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager
avg = make_averager()
print(avg(10))


