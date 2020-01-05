from multiprocessing import Process
import time, os, threading
from threading import Thread


def learn(s):
    print(f'学习{s}中，进程号：{os.getpid()}，线程号：{threading.current_thread()}')
    time.sleep(5)
    print(f'学习{s}完毕，进程号：{os.getpid()}，线程号：{threading.current_thread()}')


class_list = ['Optimization', 'Stochastic Models', 'Financial Derivatives', 'Investment Science',
              'Introduction of Chinese Financial Market']


def multi_processes_example():
    plist = []
    for c in class_list:
        # 创建进程
        p = Process(target=learn, args=(c,))
        # 生成线程
        p.start()
        # 创建的进程加入列表
        plist.append(p)
    [p.join() for p in plist]


def multi_threads_example():
    tlist = []
    for i in class_list:
        # 创建进程
        t = Thread(target=learn, args=(i,))
        # 生成线程
        t.start()
        # 创建的进程加入列表
        tlist.append(t)
    [t.join() for t in tlist]


# multi_processes_example()
# multi_threads_example()
