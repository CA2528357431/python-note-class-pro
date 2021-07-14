# iter迭代器


a = [1, True, 'asdsad']
ite = iter(a)  # 获取可迭代对象的迭代器
v1=next(ite)   # next(迭代器对象）   获取下一个元素    每次指针后移一位
print(v1)
v2=next(ite)
print(v2)
v3=next(ite)
print(v3)       #此即为for的本质
'''
v4=next(ite)
print(v4)

for 还为我们捕获异常  使得遍历正常结束
'''

# so 若想自己的新类可迭代，则必须有 __iter__ 和  __next__
# iter next 本质上调用了类的__iter__  __next__ 方法

