import time
from datetime import datetime, date


timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

d = datetime.fromtimestamp(timestamp)      # NOTE: as always "datetime" class's object "d" includs extra info about time like: h:m:s:micro s.  😎, 
print("Date:", d)                          # which aren't available in "date" class



# Creating a date object from a timestamp
# The date class gives us the ability to create a date object from a timestamp.

# In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). This date is called the Unix epoch, because this is when the counting 
# of time began on Unix systems.

# The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds.

# To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method.

# For this purpose, we can use the time module, which provides time-related functions. One of them is a function called time() that returns the number of seconds from
#  January 1, 1970 to the current moment in the form of a float number. Take a look at the example in the editor.

# Run the code to see the output.

# If you run the sample code several times, you'll be able to see how the timestamp increments itself. It's worth adding that the result of the time function depends 
# on the platform, because in Unix and Windows systems, leap seconds aren't counted.

# NOTE: In this part of the course we'll also talk about the time module.