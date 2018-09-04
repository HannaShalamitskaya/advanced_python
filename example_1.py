import sys

sys.setrecursionlimit(1 << 20)


def func(func):
    return func(func)


func(func)
