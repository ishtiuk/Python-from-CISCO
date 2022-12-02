class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


obj_1 = ExampleClass()

obj_2 = ExampleClass(5)
obj_2.set_second(9)
                                    # NOTE: The mangling won't work if you add a private instance variable outside the class code.
obj_3 = ExampleClass(10)
obj_3.__third = 12                  # NOTE: defining private instance variable from outside of the Class won't gonna to work like a Private variable,
                                    # even we add (__) at the first, it'll also act like the general variable and accessible from anywhere....

                                    # NOTE: And the proof is in line 26, notice carefully the "__third" variable's name hadn't mangled...!! 😵‍💫, so it's a general variable.
                                    # so, to be concluded, the private and protected variables are must be defined inside of Class...!! 😎 
print(obj_1.__dict__)
print(obj_2.__dict__)
print(obj_3.__dict__)


# NOTE: Output.....
# {'_ExampleClass__first': 1}
# {'_ExampleClass__first': 5, '_ExampleClass__second': 9}
# {'_ExampleClass__first': 10, '__third': 56}