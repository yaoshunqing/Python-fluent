# encoding= utf-8  
# @Time : 2020/5/24 8:40 
# @Author : Yao
# @File : order.py 
# @Software: PyCharm

from abc import ABC, abstractclassmethod
from collections import namedtuple

Customer = namedtuple('Ccustomer', 'name fidelity')

class LineItem:

    def __init__(self ,product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC):#抽象基类

    @abstractclassmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    """为积分1000或以上顾客提供5%折扣"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1

        return discount


class LargeOrderPromo(Promotion):
    """订单中不同商品达到10个以上给7折"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


joe = Customer('John', 0)
ann = Customer('Ann', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

long_order = [LineItem(str(index), 1, 1.0) for index in 'abcdefghijklmnopq']
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(ann, long_order, LargeOrderPromo()))



