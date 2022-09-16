# You could say that:

# 1. the name of an ordinary variable is the name of its content;
# 2. the name of a list is the name of a memory location where the list is stored.
# 3. Read these two lines once more - the difference is essential for understanding what we are going to talk about next.

# The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.

# How do you cope with that?

# like below

a = [45, 876, 87]      
b = a

b[0] = 9855
print(b, a)         # changes of one effects another ;)


# but here'll no effects .
# Fortunately, the solution is at your fingertips - its name is the slice.

# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

# It actually copies the list's contents, not the list's name.

# like below......

c =  b[:]
b[1] = 56
c[1] = 2

print(b, c)            # here, it doesn't effect each other, here, "c" is the brand new copy of list "b", it just copies the list contents. Not the memory location ;D
