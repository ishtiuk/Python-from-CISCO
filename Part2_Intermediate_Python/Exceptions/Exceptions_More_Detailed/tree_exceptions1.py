
# Exceptions: continued
# Look at the code in the editor. It is a simple example to start with. Run it.

# The output we expect to see looks like this:

# Oooppsss...
# THE END.

# Now look at the code below:

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")


# Something has changed in it - we've replaced ZeroDivisionError with ""ArithmeticError"".

# You already know that ""ArithmeticError"" is a general class including (among others) the ""ZeroDivisionError"" exception.

# Thus, the code's output remains unchanged. Test it.

# This also means that replacing the exception's name with either ""Exception"" or ""BaseException"" won't change the program's behavior.


# NOTE: Let's summarize:

# 1. each exception raised falls into the first matching branch;
# 2. the matching branch doesn't have to specify the same exception exactly - it's enough that the exception is more general (more abstract) than the raised one.


# NOTE: NOTE: The defalut "except" keyword reffers to the Base or Default Exception class which is ""BaseException"" or ""Exception"", 
#             that's why that can handle all exceptions....... 😎😎