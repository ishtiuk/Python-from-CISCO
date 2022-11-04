
def print_function(args, fun):
    for i in args:
        print("f(", i, ")=", fun(i), sep='')

def poly(x):
    return 2 * x ** 2 - 4 * x + 2

print_function([i for i in range(-2, 3)], poly)
print('\n')

# Can we avoid defining the poly() function, as we're not going to use it more than once? Yes, we can - this is the benefit a "lambda" can bring.

# now we're going to make the code shorter....... ;) using "lambda"....


def print_function(args, fun):
    for i in args:
        print("f(", i, ")=", fun(i), sep='')


print_function([i for i in range(-2, 3)], lambda x : 2 * x ** 2 - 4 * x + 2)


# The "print_function()" has remained exactly the same, but there is no "poly()" function. We don't need it anymore,
#  as the polynomial is now directly inside the "print_function()" invocation in the form of a "lambda" defined in the following way:

# print('fdf', 44, 545, sep='\n')