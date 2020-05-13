# encoding= utf-8  
# @Time : 2020/5/13 8:50 
# @Author : Yao
# @File : strkeydict.py 
# @Software: PyCharm
import collections
from types import MappingProxyType

class StrKeyDict0(dict):

    def __init__(self):
        super(dict, self).__init__()

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

class StrKeyDict(collections.UserDict):

    def __init__(self):
        super().__init__()

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


#使用替身代替不可变字典类型

d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d[2] = 'B'
print(d_proxy)
#d_proxy[3] = '1' 会报错











