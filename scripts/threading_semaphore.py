from threading import Semaphore
from threading import Thread
import time


def number_writer(sem, name, n_from, n_to):
    # for number in range(0, 101, 2):
    for number in range(n_from, n_to, 2):
        with sem:
            print(name, ':', number)
        time.sleep(0.1)


if __name__ == "__main__":
    semaphore = Semaphore(1)

    thread_odd = Thread(target=number_writer,
                        args=(semaphore, "Odd ", 0, 101))
    thread_even = Thread(target=number_writer,
                         args=(semaphore, "Even", 1, 101))

    thread_odd.start()
    time.sleep(0.05)
    thread_even.start()

    thread_odd.join()
    thread_even.join()
