# 斐波那契数列迭代

# 上一讲我们通过迭代器类使一个类可迭代，那么本次我们直接合并成为一个整体

class fiberit:
    def __init__(self, x):
        self.data = [0, 1]
        self.parser = 1
        self.limit = x

    def __iter__(self):
        return self

    def __next__(self):
        if self.parser < self.limit:
            x = self.data[self.parser] + self.data[self.parser - 1]
            self.parser += 1
            self.data.append(x)
            return x
        else:
            raise StopIteration


fi = fiberit(10)
for x in fi:
    print(x)

