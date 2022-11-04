
# Exceptions: continued
# The raise instruction may also be utilized in the following way (note the absence of the exception's name):

# raise


# There is one serious restriction: this kind of raise instruction may be used inside the except branch only; using it in any other context causes an error.

# The instruction will immediately re-raise the same exception as currently handled.


def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise                           # NOTE: this kinds of "raise" can be only declared inside of "except" block to raise the previously handled Error AGAIN.......!!


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")


# Thanks to this, you can distribute the exception handling among different parts of the code.

# Look at the code in the editor. Run it - we'll see it in action.

# The ZeroDivisionError is raised twice:

# first, inside the try part of the code (this is caused by actual zero division)
# second, inside the except part by the raise instruction.
# In effect, the code outputs:

# I did it again!
# I see!
# THE END.