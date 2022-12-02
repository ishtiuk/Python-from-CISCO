
# The center() method

# NOTE: The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field of a specified width.
# The centering is actually done by adding some spaces before and after the string.
# Don't expect this method to demonstrate any sophisticated skills. It's rather simple.


print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')


# NOTE: The two-parameter variant of center() makes use of the character from the second argument, instead of a space. Analyze the example below:

print('[' + 'gamma'.center(20, '*') + ']')