

# Operations on strings: ord()
# If you want to know a specific character's ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).

# The function needs a one-character string as its argument - breaching this requirement causes a TypeError exception, and returns a number representing the argument's code point.

# Look at the code in the editor, and run it. The snippet outputs:

# 97
# 32

# Now assign different values to char_1 and char_2, e.g., α (Greek alpha), and ę (a letter in the Polish alphabet); then run the code and see what result it outputs. 
# Carry out your own experiments.


# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space
alpha = 'α'

print(ord(char_1))
print(ord(char_2))

print(ord(alpha))


# chr() function for reverse

print(chr(32))
print(chr(97))