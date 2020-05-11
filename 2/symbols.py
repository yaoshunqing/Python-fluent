# encoding= utf-8  
# @Time : 2020/5/11 14:42 
# @Author : Yao
# @File : symbols.py 
# @Software: PyCharm

#两种方式
symbols = 'ABCDE'
beyond_ascii = [ord(s) for s in symbols if ord(s) < 127]
print(beyond_ascii)
beyond_ascii2 = list(filter(lambda c: c < 127, map(ord, symbols)))
print(beyond_ascii2)

#笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

#嵌套元组
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

#:实现空格，让表格工整
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longtitude) in metro_areas:
    if longtitude <= 0:
        print(fmt.format(name, latitude, longtitude))
