
# How Python finds properties and methods: continued
# Look at the code in the editor. We've modified it to show you another method of accessing any entity defined inside the superclass.

# In the last example, we explicitly named the superclass. In this example, we make use of the super() function, 
# which accesses the superclass without needing to know its name:

# NOTE: super().__init__(name)


# NOTE: The super() function creates a context in which you don't have to (moreover, you mustn't) pass the "self" argument to
#  the method being invoked - this is why it's possible to activate the superclass constructor using only one argument.

# NOTE: you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the
# resources available inside the superclass.


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)
