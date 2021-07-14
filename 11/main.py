import urllib.request
import gevent
import time

# 使得gevent可以识别全部耗时活动，无需sleep激活
from gevent import monkey

monkey.patch_all()

web1 = 'https://wallpaperm.cmcm.com/ea0bd73e3680cc91d058593797d147d9.jpg'
web2 = 'https://www.flrhbz.com/static/upload/image/original/7D365CEB05A7469421A27382F68D2D80.jpg'
web3 = 'https://www.helloimg.com/images/2020/06/14/----4k3840x2160_44beb151ba0ed069.jpg'
web4 = 'https://wallpaperm.cmcm.com/68b7b773f43be247aa8a6d2f027c32c8.jpg'


def find(web, x):
    re = urllib.request.urlopen(web)
    with open('./pic/' + str(x) + '.jpg', 'wb') as fi:
        while True:
            data = re.read(512)
            if data:
                fi.write(data)
            else:
                break


if __name__ == '__main__':
    t1 = time.time()
    a1 = gevent.spawn(find, web1, 1)
    a2 = gevent.spawn(find, web2, 2)
    a3 = gevent.spawn(find, web3, 3)
    a4 = gevent.spawn(find, web4, 4)
    gevent.joinall([a1, a2, a3, a4])
    # 等待内部步骤全部结束

    t2 = time.time()

    print('fast: ', t2 - t1)

    t3 = time.time()
    find(web1, 5)
    find(web2, 6)
    find(web3, 7)
    find(web4, 8)
    t4 = time.time()

    print('slow: ', t4 - t3)
