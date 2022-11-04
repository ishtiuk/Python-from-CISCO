class Fibo:
    def __init__(self, n=0, s=0):                     # we've defined default starting and ending values to prevent the possiblities of encountering Errors... ;)
        print("__init__ exe")
        self.__n = n - s
        self.__i = 0
        self.__a = self.__b = 1

    def __iter__(self):
        print("__iter__ exe")
        return self

    def __next__(self):
        print("__next__ exe")
        self.__i += 1

        if self.__i in [1, 2]:
            return 1
        if self.__i > self.__n:
            raise StopIteration

        c = self.__a + self.__b
        self.__b = self.__a
        self.__a = c

        return c


for i in Fibo(10):
    print(i)