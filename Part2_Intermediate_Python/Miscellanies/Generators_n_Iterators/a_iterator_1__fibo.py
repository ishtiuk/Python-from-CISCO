
def fibo(n):
    a = b = 1
    c = 0

    if n > 0 and n <= 2:
        return a

    for i in range(3, n+1):
        c = a + b
        b = a
        a = c

    return c


print(fibo(5))