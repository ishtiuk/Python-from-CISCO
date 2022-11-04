# Errors, failures, and other plagues
# Anything that can go wrong, will go wrong.

# This is Murphy's law, and it works everywhere and always. Your code's execution can go wrong, too. If it can, it will.

# Look the code in the editor. There are at least two possible ways it can "go wrong". Can you see them?

# As a user is able to enter a completely arbitrary string of characters, there is no guarantee that the string can be converted into a float value - this is the first vulnerability of the code;
# the second is that the sqrt() function fails if it gets a negative argument.
# You may get one of the following error messages.

# Something like this:

# Enter x: Abracadabra

# Traceback (most recent call last):

#   File "sqrt.py", line 3, in <module>

#     x = float(input("Enter x: "))

# ValueError: could not convert string to float: 'Abracadabra'
# output

# Or something like this:

# Enter x: -1

# Traceback (most recent call last):

#   File "sqrt.py", line 4, in <module>

#     y = math.sqrt(x)

# ValueError: math domain error
# output

# Can you protect yourself from such surprises? Of course you can. Moreover, you have to do it in order to be considered a good programmer.



import math

x = float(input("Enter x: "))
y = math.sqrt(x)

# or
# y = x ** (1 / 2)         # or 0.5

print("The square root of", x, "equals to:", y)
