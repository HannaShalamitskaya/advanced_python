from threading import Event
from threading import Thread
import time


def print_number(name, ev, start_from, count):
    for number in range(start_from, count, 2):
        ev.wait()
        ev.clear()
        time.sleep(0.1)
        print("%s: %s" % (name, number))
        ev.set()
        time.sleep(0.1)


if __name__ == "__main__":
    print_event = Event()
    print_event.set()

    thread_odd = Thread(target=print_number,
                        args=('odd ', print_event, 0, 101))
    thread_even = Thread(target=print_number,
                         args=('even', print_event, 1, 101))

    thread_odd.start()
    thread_even.start()

    thread_odd.join()
    thread_even.join()
