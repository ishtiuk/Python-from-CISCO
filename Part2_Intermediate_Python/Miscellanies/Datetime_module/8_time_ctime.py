
import time

timestamp = 1572879180
print(time.ctime(timestamp))     # NOTE: The time module provides a function called "ctime", which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.

# "ctime" stands for "convert into time"  ;)


timestamp = time.time()
print(time.ctime(timestamp))



# The time module provides a function called ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.

# Do you remember the result of the time function? That's what you need to pass to ctime. Take a look at the example in the editor.

# Result:

# Mon Nov  4 14:53:00 2019
# output

# The ctime function returns a string for the passed timestamp. In our example, the timestamp expresses November 4, 2019 at 14:53:00.

# It's also possible to call the ctime function without specifying the time in seconds. In this case, the current time will be returned:

import time
print(time.ctime())



