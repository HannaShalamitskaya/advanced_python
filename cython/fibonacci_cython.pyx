from __future__ import print_function
from datetime import datetime

_now = datetime.now


def fibn_cython(n):
    """ Print the Fibonacci series up to n """
    a, b = 0, 1

    print("Cython method")
    start = _now()

    while b < n:
        print(b, end=' ')
        a, b = b, a + b

    finish = _now()
    elapsed = finish - start
    print("\nExecution time:", elapsed.total_seconds())
