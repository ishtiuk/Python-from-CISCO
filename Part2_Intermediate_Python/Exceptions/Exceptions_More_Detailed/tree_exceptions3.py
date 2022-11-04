# Exceptions: continued
# If you want to handle two or more exceptions in the same way, you can use the following syntax:

# try:
#     :
# except (exc1, exc2):
#     :


# You simply have to put all the engaged exception names into a comma-separated list and not to forget the parentheses.


# NOTE: If an exception is raised inside a function, it can be handled:

# 1. inside the function;
# 2. outside the function;
# Let's start with the first variant - look at the code in the editor.

# The ZeroDivisionError exception (being a concrete case of the ArithmeticError exception class) is raised inside the bad_fun() function, and it doesn't leave the function - the function itself takes care of it.

# The program outputs:

# Arithmetic problem!
# THE END.



# It's also possible to let the exception propagate outside the function. Let's test it now.

# Look at the code below:
# Inside of the Function:  

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")



# Outside of the Function:

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")


# The problem has to be solved by the invoker (or by the invoker's invoker, and so on).

# The program outputs:

# What happened? An exception was raised!
# THE END.




# NOTE: the exception raised can cross function and module boundaries, and travel through the invocation chain looking for a matching except clause able to handle it.

# If there is no such clause, the exception remains unhandled, and Python solves the problem in its standard way - by terminating your code and emitting a diagnostic message.

# Now we're going to suspend this discussion, as we want to introduce you to a brand new Python