

# NOTE: The capitalize() method does exactly what it says - it creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:

# 1. if the first character inside the string is a letter (note: the first character is an element with an index equal to 0, not just the first visible character), 
#     it will be converted to upper-case;
# 2. all remaining letters from the string will be converted to lower-case.


print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
print("HelLo, Night city!".capitalize())

