
# NOTE: The replace() method
# The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.

# Look at the example code in the editor. Run it.

# The example outputs:

# www.pythoninstitute.org
# Thare are it!
# Apple
# output

# If the second argument is an empty string, replacing is actually removing the first argument's string. What kind of magic happens if the first argument is an empty string?


# NOTE: The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.

# Look at the modified example code below:

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))


# Can you guess its output? Run the code and check your guesses.


