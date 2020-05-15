# encoding= utf-8  
# @Time : 2020/5/15 14:16 
# @Author : Yao
# @File : tag.py 
# @Software: PyCharm

def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' %(attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %(name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('br', 'hello', 'world'))
print(tag('br', 'hello', cls='br-wrapper', style='{color:red}'))
print(tag(name='img',content='hello', src='./hh.jpg'))

#这个写法是b为关键字参数，需要指定
def f(a,*c,b):
    if c:
        return (a,b,[i for i in c])
    else: return (a, b)

print(f(1,2,3,b=2))
#放在*定位参数后面的关键字参数要写清楚(b=)
#print(f(1,2))会报错
print(f(1,b=2))
