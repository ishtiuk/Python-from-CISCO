
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")
print(obj)



class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    # def __init__(self, name):
    #     Super.__init__(self, name)
    pass


obj = Sub("Andy")
print(obj)





# NOTE: How Python finds properties and methods
# Now we're going to look at how Python deals with inheriting methods.

# Take a look at the example in the editor. Let's analyze it:

# 1. there is a class named Super, which defines its own constructor used to assign the object's property, named name.
# 2. the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.
# 3. the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which invokes the 
#    one from the superclass. Note how we've done it: Super.__init__(self, name).
# 4. we've explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed arguments.
# 5. we've instantiated one object of class Sub and printed it.
#    The code outputs:

# My name is Andy.


# NOTE: As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class. 
# This means that the __str__() method has been inherited by the Sub class.