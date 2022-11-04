
# More about list comprehensions: continued
# Look at the example in the editor.
# Compactness and elegance - these two words come to mind when looking at the code.

# So, what do they have in common, generators and list comprehensions? Is there any connection between them? Yes. A rather loose connection, but an unequivocal one.
# Just one change can turn any list comprehension into a generator.

# List comprehensions vs. generators
# Now look at the code below and see if you can find the detail that turns a list comprehension into a generator:

# It's the parentheses. The brackets make a comprehension, the parentheses make a generator.


the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()



for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

