
class Classy:
    def __init__(self, value) -> None:
        self.value = value


obj_1 = Classy("object")
print(obj_1.value)



        
# NOTE: that the constructor:

# 1. cannot return a value, as it is designed to return a newly created object and nothing else;
# 2. cannot be invoked directly either from the object or from inside the class (you can invoke a 
# constructor from any of the object's subclasses, but we'll discuss this issue later.)
