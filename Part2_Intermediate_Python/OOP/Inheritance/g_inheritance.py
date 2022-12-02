
# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)


# NOTE: How Python finds properties and methods: continued
# Let's try to do something similar, but with properties (more precisely: with class variables).

# Take a look at the example in the editor.

# As you can see, the Super class defines one class variable named supVar, and the Sub class defines a variable named subVar.

# Both these variables are visible inside the object of class Sub - this is why the code outputs:

# 2
# 1