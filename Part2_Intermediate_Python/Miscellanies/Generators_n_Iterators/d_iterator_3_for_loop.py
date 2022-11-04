
class My_range:
    def __init__(self, n):
        self.__n = n
        self.__val = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__val += 1

        if self.__val == (self.__n):
            raise StopIteration
        
        return self.__val
    

for i in My_range(55):
    print(i)