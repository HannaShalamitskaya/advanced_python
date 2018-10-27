from fibonacci_cython import fibn_cython
from timeit import timeit


def test():
    fibn_cython(100000000)


if __name__ == "__main__":
    timeit(test, number=100)
