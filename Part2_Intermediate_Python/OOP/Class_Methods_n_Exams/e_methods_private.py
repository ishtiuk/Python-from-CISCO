

class Classy:
    def __init__(self, val = None):
        self.val = val

    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")



obj._Classy__hidden()

print(hasattr(Classy, "_Classy__hidden"))

print(hasattr(Classy, "val"))
print(hasattr(obj, "val"))