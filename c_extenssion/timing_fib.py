from fibonacci import fibn
from timeit import timeit


def test():
    fibn(100000000)


if __name__ == "__main__":
    timeit(test, number=100)
