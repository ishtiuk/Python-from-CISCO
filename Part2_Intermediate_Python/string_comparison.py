
# Comparing strings
# Python's strings can be compared using the same set of operators which are in use in relation to numbers.

# Take a look at these operators - they can all compare strings, too:

# ==
# !=
# >
# >=
# <
# <=
# There is one "but" - the results of such comparisons may sometimes be a bit surprising. Don't forget that Python is not aware (it cannot be in any way) of subtle linguistic issues - it just compares code point values, character by character.

# The results you get from such an operation are sometimes astonishing. Let's start with the simplest cases.


# Two strings are equal when they consist of the same characters in the same order. By the same fashion, two strings are not equal when they don't consist of the same characters in the same order.

# Both comparisons give True as a result:

# 'alpha' == 'alpha'
# 'alpha' != 'Alpha'



# The final relation between strings is determined by comparing the first different character in both strings (keep ASCII/UNICODE code points in mind at all times.)

# When you compare two strings of different lengths and the shorter one is identical to the longer one's beginning, the longer string is considered greater.

# Just like here:

# 'alpha' < 'alphabet'


# The relation is True.

# String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case).

# The expression is True:

print('beta' > 'Beta')