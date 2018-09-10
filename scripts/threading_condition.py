import time
from threading import Thread
from threading import Condition

number = 0
printed = False


def is_number_even():
    if not printed and number > 0 and number % 2 == 0:
        return True
    return False


def is_number_odd():
    if not printed and number % 2 != 0:
        return True
    return False


def printer(cv, predicate, name):
    global printed
    global number

    # for num in range(10):
    while True:
        with cv:
            cv.wait_for(predicate)
            print("%s: %s" % (name, number))
            printed = True
        time.sleep(0.05)


def producer(cv):
    global number
    global printed

    for num in range(1, 101):
        with cv:
            number = num
            printed = False
            cv.notifyAll()
        time.sleep(0.1)


if __name__ == "__main__":
    condition = Condition()
    condition_thread_odd = Thread(target=printer, args=(condition, is_number_odd, "odd "))
    condition_thread_even = Thread(target=printer, args=(condition, is_number_even, "even"))
    producer_thread = Thread(target=producer, args=(condition, ))

    condition_thread_odd.start()
    condition_thread_even.start()
    producer_thread.start()

    producer_thread.join()
