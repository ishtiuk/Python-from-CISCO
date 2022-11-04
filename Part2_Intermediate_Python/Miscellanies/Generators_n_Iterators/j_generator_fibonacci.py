
def fibo_generator(n):
    a = b = 1
    c = 0

    for i in range(1, n+1):
        if i in [1, 2]:
            yield i

        else:
            c = a + b
            b = a
            a = c
            
            # a, b = c, a        # it's alos valid swapping ;)
            yield c


fibs = list(fibo_generator(10))
print(fibs)