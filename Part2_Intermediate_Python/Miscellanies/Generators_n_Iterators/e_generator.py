
def generator(n):

    for i in range(n):
        yield i



for n in generator(10):
    print(n)


gen = generator(5)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())           # it'll return StopIteration Error 

# NOTE: "yield" must be used inside from function....  it's not applicable in outside of function....
