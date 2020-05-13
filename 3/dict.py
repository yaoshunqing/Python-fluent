# encoding= utf-8  
# @Time : 2020/5/13 7:47 
# @Author : Yao
# @File : dict.py 
# @Software: PyCharm

import sys
import re
import collections

# 创建字典的多种方式
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})
print(a == b == c == d == e)

# 字典推导
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

# 将一个元组列表转换为字典
country_code = {country: code for code, country in DIAL_CODES if code < 66}
print(country_code)

#统计单词出现情况
WORD_RE = re.compile(r'\w+')
#index = {}
index = collections.defaultdict(list)
with open('../.gitignore', encoding='utf-8') as fp:
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标(从1开始)
    for line_no, line in enumerate(fp, 1):
        #finditer用于循环，依次迭代值
        for match in WORD_RE.finditer(line):
            #正则表达式中，group()用来提出分组截获的字符串，()用来分组
            #不能直接使用match，它是一个类
            word = match.group(0)
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现， 这样写只是为了证明论点
            #occurrences = index.get(word, [])
            #occurrences.append(location)
            #index[word] = occurrences
            #精简写法,上文使用index={}
            #index.setdefault(word, []).append(location)
            #使用defaultdict
            index[word].append(location)
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])


#使用counter统计单词各个字母出现次数
ct = collections.Counter('happy')
print(ct)
ct.update('happy')
print(ct)