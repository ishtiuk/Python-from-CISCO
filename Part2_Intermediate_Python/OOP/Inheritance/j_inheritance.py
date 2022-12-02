
# How Python finds properties and methods: continued
# Multiple inheritance occurs when a class has more than one superclass. Syntactically, such inheritance 
# is presented as a comma-separated list of superclasses put inside parentheses after the new class name - just like here:

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())


# The Sub class has two superclasses: SuperA and SuperB. This means that the Sub class inherits all the goods offered by both SuperA and SuperB.

# The code prints:

# 10 11
# 20 21
# output

# Now it's time to introduce a brand new term - overriding.

# What do you think will happen if more than one of the superclasses defines an entity of a particular name?