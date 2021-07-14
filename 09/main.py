# gevent

# 识别耗时活动，自动切换
import gevent
import time


def w1(x):
    for _ in range(x):
        print('w1 ing')
        gevent.sleep(0)  # 唤醒
        # 也可以不写0，通过比例设置执行关系
        # 如gevent.sleep(0.1)和gevent.sleep(0.3)的步骤执行比为3：1


def w2(x, y):
    s = 0
    for r in range(0, x):
        s += r ** y
        gevent.sleep(0)
    print(s, '*' * 50)


def w3(x):
    for _ in range(x):
        print('w3 ing', gevent.getcurrent())  # 获取当前协程
        gevent.sleep(0)


# 通过调节gevent.sleep的参数来自动调节两个协程切换


if __name__ == '__main__':
    g1 = gevent.spawn(w1, 100)
    g2 = gevent.spawn(w2, 12, 16)
    g3 = gevent.spawn(w3, 300)
    # 指派任务

    g1.join()
    g3.join()
    g2.join()

    print('finish')
