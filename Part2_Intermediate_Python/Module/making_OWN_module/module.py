print("I'l like to be a module")
print(__name__)


""" module.py - an example of a Python module """


__counter = 0

def suml(my_list):
    global __counter
    __counter += 1

    sums = 0

    for elem in my_list:
        sums += elem
    return sums

def prodl(my_list):
    global __counter
    __counter += 1    

    prod = 1

    for elem in my_list:
        prod *= elem
    return prod

if __name__ == '__main__':
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]

    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
