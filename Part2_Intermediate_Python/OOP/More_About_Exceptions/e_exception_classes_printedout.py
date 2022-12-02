# Exceptions are classes
# All the built-in Python exceptions form a hierarchy of classes. There is no obstacle to extending it if you find it reasonable.

# Look at the code in the editor.

# This program dumps all predefined exception classes in the form of a tree-like printout.

# As a tree is a perfect example of a recursive data structure, a recursion seems to be the best tool to traverse through it. 
# The print_exception_tree() function takes two arguments:

# a point inside the tree from which we start traversing the tree;
# a nesting level (we'll use it to build a simplified drawing of the tree's branches)
# Let's start from the tree's root - the root of Python's exception classes is the BaseException class (it's a superclass of all other exceptions).

# For each of the encountered classes, perform the same set of operations:

# print its name, taken from the __name__ property;
# iterate through the list of subclasses delivered by the __subclasses__() method, and recursively invoke the print_exception_tree() 
# function, incrementing the nesting level respectively.
# Note how we've drawn the branches and forks. The printout isn't sorted in any way - you can try to sort it yourself, if you want a 
# challenge. Moreover, there are some subtle inaccuracies in the way in which some branches are presented. That can be fixed, too, if you wish.



def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("    |" * (nest - 1), end='')
    if nest > 0:
        print("    +---", end='')

    print(thisclass.__name__)

    for subcls in thisclass.__subclasses__():
        print_exception_tree(subcls, nest + 1)


print_exception_tree(BaseException)
