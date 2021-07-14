# 迭代器

#构造属于你的可迭代

class mylist:
    def __init__(self):
        self.item=[]
    def add(self,x:list):
        self.item.append(x)
    def __iter__(self):
        it=myiter(self.item)

        return it

class myiter:
    def __init__(self,item:list):
        self.data=item.copy()
        self.paser=0
    def __next__(self):
        if self.paser<len(self.data):
            da=self.data[self.paser]
            self.paser+=1
            return da
        else:
            raise StopIteration # 停止迭代

if __name__ == '__main__':
    li=mylist()
    li.add(['caoan','cool',True])
    li.add(['hmr', 'person', False])
    li.add(['world', 'good', False])
    print(li.item)
    for x in li:
        print(x)


    print('-'*50)

    ite=iter(li)

    v1=next(ite)
    print(v1)
    v2 = next(ite)
    print(v2)
    v3 = next(ite)
    print(v3)