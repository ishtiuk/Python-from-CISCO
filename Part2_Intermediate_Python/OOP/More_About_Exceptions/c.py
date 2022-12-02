# Exceptions are classes
# All the previous examples were content with detecting a specific kind of exception and responding to it in an appropriate way. Now we're going to
#  delve deeper, and look inside the exception itself.

# You probably won't be surprised to learn that exceptions are classes. Furthermore, when an exception is raised, an object of the class is instantiated,
#  and goes through all levels of program execution, looking for the except branch that is prepared to deal with it.

# Such an object carries some useful information which can help you to precisely identify all aspects of the pending situation. To achieve that goal,
#  Python offers a special variant of the exception clause - you can find it in the editor.

# As you can see, the except statement is extended, and contains an additional phrase starting with the as keyword, followed by an identifier. The 
# identifier is designed to catch the exception object so you can analyze its nature and draw proper conclusions.

# Note: the identifier's scope covers its except branch, and doesn't go any further.

# The example presents a very simple way of utilizing the received object - just print it out (as you can see, the output is produced by the object's 
# __str__() method) and it contains a brief message describing the reason.

# The same message will be printed if there is no fitting except block in the code, and Python is forced to handle it alone.



try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
