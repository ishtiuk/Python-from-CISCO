
# Exceptions: continued
# The ""raise"" instruction raises the specified exception named exc as if it was raised in a normal (natural) way:

# raise exc


# NOTE: ""raise"" is a keyword.


# The instruction enables you to:

# 1. simulate raising actual exceptions (e.g., to test your handling strategy)
# 2. partially handle an exception and make another part of the code responsible for completing the handling (separation of concerns).
# 3. Look at the code in the editor. This is how you can use it in practice.

# The program's output remains unchanged.

# In this way, you can test your exception handling routine without forcing the code to do stupid things.


def bad_fun(n):
    raise ZeroDivisionError("[error forced..!]")


try:
    bad_fun(0)
except ArithmeticError as err:
    print("What happened? An error?", err)

print("THE END.")
