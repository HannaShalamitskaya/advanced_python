import time
from threading import Timer


def print_number(name, start_from, end_with, delay):
    for number in range(start_from, end_with, 2):
        print("%s: %s" % (name, number))
        time.sleep(delay)


if __name__ == "__main__":
    thread_odd = Timer(0.05, print_number, ("odd ", 0, 101, 0.1))
    thread_even = Timer(0.1, print_number, args=("even", 1, 101, 0.1))

    thread_odd.start()
    thread_even.start()

    thread_odd.join()
    thread_even.join()
