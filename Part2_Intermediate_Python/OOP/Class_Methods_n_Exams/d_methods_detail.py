

# NOTE: The example in the editor shows how to define a constructor with a default argument value. Test it.
# The code outputs:


class Classy:
    def __init__(self, val =  None):
        self.val = val



obj_1 = Classy("object")
obj_2 =  Classy()

print(obj_1.val, obj_2.val)

print(Classy.__dict__)
print(obj_1.__dict__)