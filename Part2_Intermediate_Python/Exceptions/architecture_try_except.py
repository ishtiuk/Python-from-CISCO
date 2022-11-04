
# NOTE: Key takeaways

# 1. An exception is an event in a program execution's life caused by an abnormal situation. The exception should he handled to avoid program termination. 
# The part of your code that is suspected of being the source of the exception should be put inside the try branch.

# When the exception happens, the execution of the code is not terminated, but instead jumps into the except branch. This is the place where the handling 
# of the exception should take place. The general scheme for such a construction looks as follows:

# :
# The code that always runs smoothly.
# :
try:

    # Risky code.
    pass
except:
    
    # Crisis management takes place here.
    pass

# Back to normal.
print("Danger(1) zone has passed...")


# 2. NOTE: If you need to handle more than one exception coming from the same try branch ,you can add more than one except branch, 
# but you have to label them with different exception names, like this:


# The code that always runs smoothly.

try:

    # Risky code.
    pass

except ValueError:
    # Crisis management takes place here.
    pass
except KeyboardInterrupt:
    # We save the world here.
    pass

print("Danger(2) zone has passed...")
# Back to normal.



# At most, one of the except branches is executed – none of the branches is performed when the raised exception doesn't match to the specified exceptions.


# 3. You cannot add more than one anonymous (unnamed) except branch after the named ones.


# The code that always runs smoothly.

try:
   
    # Risky code.
    pass

except IndentationError:
    # Crisis management takes place here.
    pass
except IndexError:
    # We save the world here.
    pass
except:
    # All other issues fall here.
    pass


print("Danger(3) zone has passed...")
# Back to normal.
