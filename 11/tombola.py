# encoding= utf-8  
# @Time : 2020/6/1 20:12 
# @Author : Yao
# @File : tombola.py 
# @Software: PyCharm

from abc import ABC,abstractmethod

class Tombola(ABC):

    @abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
        如果实例为空，抛出lookupError"""

    def loaded(self):
        """如果至少有一个元素，返回True，否则False"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组"""
        items =[]

        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(sorted(items))




