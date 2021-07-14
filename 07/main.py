# 协程 yield

# 协程的地位低于线程
# 协程本质是在多个函数之间来回切换，达成‘同时执行’的外表
# 协程会保存yield之前的数据
# 由于只是在函数之间切换因此效率高

import time

def w1():
    while True:
        print('w1 ing')
        yield
def w2():
    while True:
        print('w2 ing')
        yield

if __name__ == '__main__':
    ww1=w1()
    ww2=w2()
    while True:
        next(ww1)
        next(ww2)