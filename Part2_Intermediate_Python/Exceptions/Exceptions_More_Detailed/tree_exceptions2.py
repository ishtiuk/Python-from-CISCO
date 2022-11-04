# Exceptions: continued
# Look at the code in the editor. What will happen here?

# NOTE: The first matching branch is the one containing ""ZeroDivisionError"". It means that the console will show:

# Zero division!
# THE END.
# output

# Will it change anything if we swap the two except branches around? Just like here below:

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")


# NOTE: The change is radical - the code's output is now:

# Arithmetic problem!
# THE END.
# output

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

# Why, if the exception raised is the same as previously?

# The exception is the same, but the more general exception is now listed first - it will catch all zero divisions too. It also means that there's no 
# chance that any exception hits the ""ZeroDivisionError"" branch. This branch is now completely unreachable.

# NOTE: Remember:

# the order of the branches matters!
# don't put more general exceptions before more concrete ones;
# this will make the latter one unreachable and useless;
# moreover, it will make your code messy and inconsistent;
# Python won't generate any error messages regarding this issue.

