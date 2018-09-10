from multiprocessing import freeze_support
from multiprocessing import Lock
from multiprocessing import Process
from multiprocessing import Queue
import os
import time


def generate_numbers(queue, count):
    for num in range(count + 1):
        queue.put(num)
        time.sleep(0.1)


def print_numbers(queue, lock):
    while not queue.empty():
        with lock:
            num = queue.get()
            print("%s:" % os.getpid(), num)
        time.sleep(0.5)


if __name__ == '__main__':
    freeze_support()
    pq = Queue()
    pl = Lock()

    p = Process(target=generate_numbers, args=(pq, 100))
    pn1 = Process(target=print_numbers, args=(pq, pl))
    pn2 = Process(target=print_numbers, args=(pq, pl))

    p.start()
    time.sleep(0.05)
    pn1.start()
    time.sleep(0.05)
    pn2.start()

    p.join()
    pn1.join()
    pn2.join()

    p.terminate()
    pn1.terminate()
    pn2.terminate()
