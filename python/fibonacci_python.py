
def fibn_python(n):
    print("Python method")
    a, b = 0, 1

    while b < n:
        print(b, end=' ')
        a, b = b, a + b
