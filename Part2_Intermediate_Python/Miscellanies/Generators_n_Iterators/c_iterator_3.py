class Fib:
    def __init__(self, n):
        self.__n = n
        self.__i = 0
        self.__a = self.__b = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        print("Fib next")
        self.__i += 1

        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1

        c = self.__a + self.__b
        self.__b = self.__a
        self.__a = c

        return c

class Class(Fib):
    def __init__(self, n):
        self.__iter__ = Fib(n)

    def __iter__(self):
        print("Class Iter")
        return self.__iter__


obj = Class(10)

for i in obj:
    print(i)
