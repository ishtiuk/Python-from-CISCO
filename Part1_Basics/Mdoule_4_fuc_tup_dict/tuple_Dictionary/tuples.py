
# Tuple can be make by this approch too.....
tuple_1 = 1,               # remember comma ',' is accentuated here. otherwise it'll be considered as a "int"
tuple_2 = (1, )



# If you want to create a one-element tuple, you have to take into consideration the fact that, due to syntax reasons (a tuple has to be distinguishable from an ordinary, single value),
#  you must end the value with a comma:

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

print(type(tuple_1), type(tuple_2), type(one_element_tuple_1))


my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)



# let's make the copy of an element

print(my_tuple[1:2] * 5)

# see the differences.......... ;D
print(my_tuple[1] * 5)    # ;D

