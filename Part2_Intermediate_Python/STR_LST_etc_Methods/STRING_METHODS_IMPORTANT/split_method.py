
# NOTE: The split() method
# The split() method does what it says - it splits the string and builds a list of all detected substrings.

# The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation, and aren't copied into the resulting list.

# If the string is empty, the resulting list is empty too.

# Look at the code in the editor. The example produces the following output:

# ['phi', 'chi', 'psi']
# output

# Note: the reverse operation can be performed by the join() method.


# Demonstrating the split() method:
print("phi       chi\npsi".split())


print(''.join("phi       chi\npsi".split()))