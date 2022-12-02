

# Uppercase letters are considered as minimum that means low value because of ASCII code system the uppercase "Z" value is "90"
# and Lowercase "a" value is 97.

# now, you might be able to visulize the reason behind the considering UPPERCASE as lower value and LOWERCASE as higher value. ;)




# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
print(max("aAbByYzZ"))

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

# here, "space" ASCII value is 32 lower from the others, that's why space has been printed. 
print(min("Abc Ed Xuu"), ord(" "), chr(32))

t = [0, 1, 2]
print(min(t))


# Operations on strings: max()
# Similarly, a function named max() finds the maximum element of the sequence.
# Look at Example 1 in the editor. The example program outputs:


# Note: It's a lower-case z.
# Now let's see the max() function applied to the same data as previously. Look at Examples 2 & 3 in the editor.
# The expected output is:



# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

