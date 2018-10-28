from __future__ import print_function


def fibn_cython(n):
    """ Print the Fibonacci series up to n """
    print("Cython method")
    a, b = 0, 1

    while b < n:
        print(b, end=' ')
        a, b = b, a + b
