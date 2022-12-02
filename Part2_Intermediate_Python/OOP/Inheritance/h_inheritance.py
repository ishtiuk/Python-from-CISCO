
# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    supVar = 50
    
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)        # NOTE: as we can see that it hadn't printed the class var of it's own class, instead it had printed the superclass's instance var.
                         # cause instance var gets the "supreme privilege"  ;D
