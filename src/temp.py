from multiprocessing import freeze_support
from multiprocessing import Lock
from multiprocessing import Process
import random
import time


def generate_number(lck):
    while True:
        with lck:
            print("num:", random.randint(0, 100))
        time.sleep(1)


if __name__ == '__main__':
    freeze_support()
    lock = Lock()
    p = Process(target=generate_number, args=(lock, ))
    print("Will start")
    p.start()

    while True:
        if input() == 'q':
            with lock:
                print("Will terminate")
                p.terminate()
                break

    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
