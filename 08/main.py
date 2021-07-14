# greenlet  协程组件

import greenlet


def w1():
    while True:
        print('w1 ing')
        g2.switch()
        # 来回切换


def w2():
    while True:
        print('w2 ing')
        g1.switch()


if __name__ == '__main__':
    g1 = greenlet.greenlet(w1)
    g2 = greenlet.greenlet(w2)
    while True:
        g1.switch()
        # 从谁开始
