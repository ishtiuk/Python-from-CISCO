def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))



# A brief look at closures: continued
# A closure has to be invoked in exactly the same way in which it has been declared.

# In the example below:


# the inner() function is parameterless, so we have to invoke it without arguments.

# Now look at the code in the editor. It is fully possible to declare a closure equipped with an arbitrary number of parameters, e.g., one, just like the power() function.
# This means that the closure not only makes use of the frozen environment, but it can also modify its behavior by using values taken from the outside.

# This example shows one more interesting circumstance - you can create as many closures as you want using one and the same piece of code. This is done with a function 
# named make_closure(). Note:

# the first closure obtained from make_closure() defines a tool squaring its argument;
# the second one is designed to cube the argument.
# This is why the code produces the following output:

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# output

# Carry out your own tests.

