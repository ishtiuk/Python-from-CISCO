

# Sorting
# Comparing is closely related to sorting (or rather, sorting is in fact a very sophisticated case of comparing).

# This is a good opportunity to show you two possible ways to sort lists containing strings. Such an operation is very common in the real world - any time you see a list of names, goods, titles, or cities, you expect them to be sorted.

# Let's assume that you want to sort the following list:

#  greek = ['omega', 'alpha', 'pi', 'gamma']


# In general, Python offers two different ways to sort lists.

# The first is implemented as a function named sorted().

# The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements. (Note: this description is a bit simplified compared to the actual implementation - we'll discuss it later.)

# The original list remains untouched.

# Look at the code in the editor, and run it. The snippet produces the following output:

# ['omega', 'alpha', 'pi', 'gamma']
# ['alpha', 'gamma', 'omega', 'pi']
# output

# The second method affects the list itself - no new list is created. Ordering is performed in situ by the method named sort().

# The output hasn't changed:

# ['omega', 'alpha', 'pi', 'gamma']
# ['alpha', 'gamma', 'omega', 'pi']
# output

# If you need an order other than non-descending, you have to convince the function/method to change its default behaviors. We'll discuss it soon.







# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

second_greek = sorted(second_greek, reverse=True)
print(second_greek)
