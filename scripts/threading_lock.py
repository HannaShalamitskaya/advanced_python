import time
from threading import Thread
from threading import Lock


class NumberThread(Thread):
    thread_lock = Lock()

    def __init__(self, start_from, finish_with, step, delay, **kwargs):
        Thread.__init__(self, **kwargs)
        self.start_from = start_from
        self.finish_with = finish_with
        self.step = step
        self.delay = delay

    def run(self):
        for number in range(self.start_from, self.finish_with+1, self.step):
            with self.thread_lock:
                print("%s: %s" % (self.name, number))
            time.sleep(self.delay)


if __name__ == "__main__":
    threads = (NumberThread(0, 100, 2, 0.2, name="thread-even"),
               NumberThread(1, 100, 2, 0.2, name="thread-odd "))

    for thread in threads:
        thread.start()
        time.sleep(0.1)

    for thread in threads:
        thread.join()
