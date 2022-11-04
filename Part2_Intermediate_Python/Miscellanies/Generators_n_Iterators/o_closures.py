def outer(par):
    loc = par

    def inner():
        return par
    return inner



var = 1
fun = outer(var)
print(fun())


# A brief look at closures
# Let's start with a definition: closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. Intricate? A bit.

# Let's analyze a simple example:

def outer(par):
    loc = par


var = 1
outer(var)

print(var)
try:
    print(loc)
except (NameError, BaseException) as err:
    print(err)



# The example is obviously erroneous.

# The last two lines will cause a NameError exception - neither par nor loc is accessible outside the function. Both the variables exist when and
#  only when the outer() function is being executed.

# Look at the example in the editor. We've modified the code significantly.
# There is a brand new element in it - a function (named inner) inside another function (named outer).

# How does it work? Just like any other function except for the fact that inner() may be invoked only from within outer(). We can say that inner()
# is outer()'s private tool - no other part of the code can access it.

# Look carefully:

# the inner() function returns the value of the variable accessible inside its scope, as inner() can use any of the entities at the disposal of outer()
# the outer() function returns the inner() function itself; more precisely, it returns a copy of the inner() function, the one which was frozen at 
# the moment of outer()'s invocation; the frozen function contains its full environment, including the state of all local variables, which also means
#  that the value of loc is successfully retained, although outer() ceased to exist a long time ago.
# In effect, the code is fully valid, and outputs:

# 1
# output

# The function returned during the outer() invocation is a closure.

# print(ZeroDivisionError.__base__)