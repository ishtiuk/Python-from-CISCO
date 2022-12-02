# More about exceptions
# The try-except block can be extended in one more way - by adding a part headed by the finally keyword (it must be the last branch of the
#  code designed to handle exceptions).

# Note: these two variants (else and finally) aren't dependent in any way, and they can coexist or occur independently.

# The finally block is always executed (it finalizes the try-except block execution, hence its name), no matter what happened earlier, even
#  when raising an exception, no matter whether this has been handled or not.

# Look at the code in the editor. It outputs:

# Everything went fine
# It's time to say good bye
# 0.5
# Division failed
# It's time to say good bye
# None


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
