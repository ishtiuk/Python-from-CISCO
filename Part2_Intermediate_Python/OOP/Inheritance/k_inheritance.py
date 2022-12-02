class Level1:
    var = 100

    def fun(self):
        return 101


class Level2:
    var = 200

    def fun(self):
        return 201


class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())


class Level4(Level1, Level2):           # once it has multiple inheritance then it will be satisfied with the first Inherited Class's entities if it contains those, 
    pass                                # otherwise it'll start to check on the first Inherited Class 🥴

obj = Level4()
print(obj.var, obj.fun())



# Both, Level1 and Level2 classes define a method named fun() and a property named var. Does this mean that the Level3 class object will be able to 
# access two copies of each entity? Not at all.

# The entity defined later (in the inheritance sense) overrides the same entity defined earlier. This is why the code produces the following output:
# 200 201
# output

# As you can see, the var class variable and fun() method from the Level2 class override the entities of the same names derived from the Level1 class.
# NOTE: This feature can be intentionally used to modify default (or previously defined) class behaviors when any of its classes needs to act in a different way to its ancestor.
# We can also say that Python looks for an entity from bottom to top, and is fully satisfied with the first entity of the desired name.