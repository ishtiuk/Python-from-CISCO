
# NOTE: The lstrip() method
# The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.

# Analyze the example code in the editor.

# The brackets are not a part of the result - they only show the result's boundaries.

# The example outputs:

# [tau ]
# output

# The one-parameter lstrip() method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:

print("www.cisco.com".lstrip("w."))


# Brackets aren't needed here, as the output looks as follows:

# cisco.com
# output

# Can you guess the output of the snippet below? Think carefully. Run the code and check your predictions.

print("pythoninstitute.org".lstrip(".org"))


# Surprised? Leading characters, leading whitespaces. Again, experiment with your own examples.

