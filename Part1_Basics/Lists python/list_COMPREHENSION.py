
# let's create a list filled by power of two...

twos = [2 ** x for x in range(8+1)]
print(twos)



# let's print all number's squres from 0 to 10

squres = [i ** 2 for i in range(10+1)]
print(squres)



# let's make a list of all odd numbers squres from 0 to 10

squres_odd = [i ** 2 for i in range(10+1) if i % 2 != 0]
print(squres_odd)




# let's make a list of all even numbers squres from 0 to 10

squres_even = [i ** 2 for i in range(10+1) if i % 2 == 0]
print(squres_even)