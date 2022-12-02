
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
print(sun)


# NOTE: the default "__str__" (which run implicitly when any object wants to be printed, hence we've not defined that explicitly) returns
#  ugly sms the object identifier memory location of the "sun" Object..... 

# Hence we can make that little bit nice looking by defining the "__str__" method explicitly..... 😎 here, we can return anything, but it will be conventient if we return 
# some instance vars or class behavior decriber string........



class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy
        
sun = Star("Sun", "Milky Way")
print(sun, sun.__str__())
print(Star.__subclasses__())