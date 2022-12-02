
# NOTE: The find() method is similar to index(), which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:

# it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
# it works with strings only - don't try to apply it to any other sequence.
# Look at the code in the editor. This is how you can use it.

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))



# NOTE: If you want to perform the find, not from the string's beginning, but from any position, you can use a two-parameter variant of the find() method. Look at the example:

print('kappa'.find('a', 2))
print('kappa'.find('a', 3))



# NOTE: There is also a three-parameter mutation of the find() method - the third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search).

# Look at our example below:

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
