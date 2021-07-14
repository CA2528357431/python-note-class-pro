# 生成器

list1=(x**2 for x in range(-3,4) )
# 创建生成器————属于迭代器

value1=next(list1)
print(value1)
value2=next(list1)
print(value2)
value3=next(list1)
print(value3)
#next出数值，同上两讲的迭代

print('-'*20)

# parser 已经移动，所以遍历不能得带
for x in list1:
    print(x)
