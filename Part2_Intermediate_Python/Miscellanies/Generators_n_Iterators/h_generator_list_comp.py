
# The list() function

# The list() function can transform a series of subsequent generator invocations into a real list:

def powers_of_2(n):
    power = 1 

    for i in range(n):
        yield power
        
        power *= 2



t = list(powers_of_2(10))
print(t)

print(3 in powers_of_2(5))       # "in" operator can be also used on generators...