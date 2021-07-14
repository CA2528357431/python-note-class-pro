# __solts__

class hk0:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class hk:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    __slots__ = ('a','b','c')
    #限制对象只能由以上属性
    #对子类无用
    #对类变量无用

x=hk0(1,2,3)
y=hk(1,2,3)

try:
    x.d=4
    print('success')
except :
    print('fail')

try:
    y.d=4
    print('success')
except :
    print('fail')