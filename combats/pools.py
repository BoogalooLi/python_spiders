import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def learn(s):
    print(f'{s}，进程号：{os.getpid()}，线程号：{threading.current_thread()}')
    time.sleep(5)
    print(f'{s} over，进程号：{os.getpid()}，线程号：{threading.current_thread()}')


class_list = ['Optimization', 'Stochastic Models', 'Financial Derivatives']

# 创建线程池与进程池
thread_pool = ThreadPoolExecutor(max_workers=len(class_list))
process_pool = ProcessPoolExecutor(max_workers=len(class_list))

# 循环任务
# 制定对应任务和参数
[thread_pool.submit(learn, c) for c in class_list]
[process_pool.submit(learn, c) for c in class_list]

# 关闭线程池与进程池
thread_pool.shutdown()
process_pool.shutdown()
