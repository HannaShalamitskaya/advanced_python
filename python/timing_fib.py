from python.fibonacci_python import fibn_python
from timeit import timeit


def test():
    fibn_python(100000000)


if __name__ == "__main__":
    timeit(test, number=100)
