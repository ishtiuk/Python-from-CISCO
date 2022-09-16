
# let's take a look about positional argument...  ;)
# Example 1:

def introduction(first_name, last_name):
    print("Hello I'm", first_name, last_name, end=".\n")


introduction("Skywalker", "Luke")
introduction(first_name="Quick", last_name="Jesse")
introduction(last_name="Kent", first_name="Clark")


# Example 2:
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(5, 45, 32)
adding(c = 5, a = 99, b = 88)

try:
    adding(3, a = 1, b = 2)
except TypeError as typerr:
    print(typerr)

adding(3, c = 1, b = 2)



# Example 3: 
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
introduction("Adam", last_name="Smasher")


# Example 4:
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction()            # it's absolutely right, because we passed the parameters already. ;)  | but yup we can override......  ;D
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
introduction("Adam", last_name="Smasher")
introduction(first_name="Adam", last_name="Smasher")