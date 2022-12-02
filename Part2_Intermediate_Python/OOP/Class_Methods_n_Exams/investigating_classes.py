
class MyClass():
    pass


obj = MyClass()

obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            
            if isinstance(val, int):
                setattr(obj, name, val + 1)
                

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


# print(isinstance(44.6, float))


superclasses = MyClass.__bases__

for i in superclasses:
    print(i.__name__)
    

class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("\n\nMy name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()

