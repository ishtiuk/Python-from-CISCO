
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)
      
try:                                   # NOTE: in my opinion it's not safe at all, because if we pass 2 or any even number instead of odd num or 1 at the time of Object
    print(example_object.b)            # defining then the var 'a' will be missing and the code will definitly return AttributeError.... 
except AttributeError:
    pass           


# NOTE: Hence, Python provides a The function is named hasattr, and expects two arguments to be passed to it:
# 1. the class or the object being checked;
# 2. the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)

# let's implement.....

x = hasattr(example_object, "a")
y = hasattr(example_object, "b")
print(x, y)


c = hasattr(ExampleClass, "a")    # NOTE: before creating Objects there will be no existance of instance varibles..... 😎🥱, that's why both "a" and "b" are False
c = hasattr(ExampleClass, "b")
print(c)

obj = hasattr(ExampleClass(3), "a")     # NOTE: here the Object has been created implicitly.... 😅
print(obj)

