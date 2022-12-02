
class Classy:
    varia = 1
    
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

print(obj.__module__)
print(Classy.__module__)

# The inner life of classes and objects: continued
# "__dict__" is a dictionary. Another built-in property worth mentioning is "__name__", which is a string.
# The property contains the name of the class. It's nothing exciting, just a string.

# NOTE: : the "__name__" attribute is absent from the object - it exists only inside classes.


class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

try:
    print(obj.__name__)            # Caused an error as I've mentioned above...
except:
    pass


def printBases(cls):
    for x in cls.__bases__:
        print(x.__name__)

printBases(Classy)