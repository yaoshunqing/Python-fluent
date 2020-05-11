# encoding= utf-8  
# @Time : 2020/5/8 15:38 
# @Author : Yao
# @File : frenchdeck.py 
# @Software: PyCharm

#从一个序列内随机选取一个元素
from random import choice
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    #按照花色加权大小计算权值
    rank_value = FrenchDeck.ranks.index(card.rank) #找到ranks中对应卡牌的位置，即[0-12]

    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FrenchDeck()
#特殊方法的存在是为了被python解释器调用的，我们使用内置函数实现就好
#不需要显式调用特殊方法
print(deck.__len__())
print(len(deck))
#print(deck[0])
print(choice(deck))
# for card in deck:
#     print(card)

for card in sorted(deck, key=spades_high):
    print(card)




