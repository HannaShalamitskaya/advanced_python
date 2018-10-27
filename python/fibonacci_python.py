import time


def fibn_python(n):
    a, b = 0, 1

    start = time.time()
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

    finish = time.time()
    elapsed = finish - start
    print("\nExecution time:", elapsed)
