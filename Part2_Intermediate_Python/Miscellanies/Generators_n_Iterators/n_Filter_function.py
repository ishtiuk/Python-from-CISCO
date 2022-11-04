
# Lambdas and the filter() function
# Another Python function which can be significantly beautified by the application of a lambda is filter().
# It expects the same kind of arguments as map(), but does something different - it filters its second argument while being guided by directions 
# flowing from the function specified as the first argument (the function is invoked for each list element, just like in map()).

# The elements which return True from the function pass the filter - the others are rejected.
# The example in the editor shows the filter() function in action.

# NOTE: we've made use of the random module to initialize the random number generator (not to be confused with the generators we've just talked about) 
# with the seed() function, and to produce five random integer values from -10 to 10 using the randint() function.

# The list is then filtered, and only the numbers which are even and greater than zero are accepted.
# Of course, it's not likely that you'll receive the same results, but this is what our results looked like:

# [6, 3, 3, 2, -7]
# [6, 2]
# output



from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)





# extra ;)
buffer = bytearray("hello i'm".encode())
line = "hello i'm"

s = open('f.txt', 'rb')
size = s.readinto(buffer)
print(buffer[7])