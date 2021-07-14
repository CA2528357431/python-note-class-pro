# 生成器

def f():
    a = 1
    yield a
    a += 3
    yield a
    a += 2
    yield a
    a += 6
    yield a
    a += 10
    # 保存上一次的全部状态
    # next时从此yield开始

def fiber(n):
    a = 0
    b = 1
    parser = 0
    while parser < n:
        a, b = b, a + b
        parser += 1
        yield a
        # 生成器第二种写法   yield相当于return，但声明了是迭代


if __name__ == '__main__':

    ff = f()
    print(next(ff))
    print(next(ff))
    print(next(ff))
    print(next(ff))

    print('_' * 50)

    fib = fiber(5)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))

# 总之生成器在迭代时远比迭代器优雅，因此想迭代就用生成器
# 当然，当遇到特殊数据阵列需要遍历而又无法用已有数据类型表示，则使用迭代器

