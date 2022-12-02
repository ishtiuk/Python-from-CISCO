
# Strings as sequences: indexing

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()


# Strings as sequences: iterating
# Iterating through the strings works, too. Look at the example below:

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# Slices

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


# Python strings are immutable
# We've also told you that Python's strings are immutable. This is a very important feature. What does it mean?

# So, we can't use the 'insert(), append(), pop()' or any other functions which are applicable for LISTS to manipulate STRINGS.
# but yeah we can add to string using '+' plus operator.          # in my opinion, STRINGS are almost Like the TUPLES. 


alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
