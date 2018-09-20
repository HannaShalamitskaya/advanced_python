from concurrent.futures import ProcessPoolExecutor
from math import sqrt
from multiprocessing import freeze_support
from time import sleep


def is_prime(number):
    sleep(0.5)
    # 0 is NOT prime
    if number == 1:
        return number
    elif not any([number % i == 0 for i in range(2, round(sqrt(number)) + 1)]):
        return number
    return 0


if __name__ == '__main__':
    freeze_support()
    n = m = None
    print("Please provide borders (N and M) for the range")

    try:
        n = int(input("N ( > 0): "))
        m = int(input("M ( > N): "))
    except ValueError:
        print("Please provide a number(s)")
    else:
        if n > m:
            print("wrong values (%s > %s). Must be N < M" % (n, m))
        else:
            prime_sum = 0
            for res in ProcessPoolExecutor(4).map(is_prime, range(n, m - 1)):
                if res:
                    print("number", res, "is prime")
                    prime_sum += res
            print("Sum of prime numbers:", prime_sum)
