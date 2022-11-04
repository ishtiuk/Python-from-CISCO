import time

# NOTE: finally got the custom "Timestamp" making approch 🤩🤩🤩

# The first of the functions, called "asctime", converts a struct_time object or a tuple to a string. NOTE: that the familiar gmtime function is used to get the struct_time object.
# If you don't provide an argument to the "asctime" function, the time returned by the localtime function will be used.

# timestamp = 1572879180

timestamp = time.time()
utc_time = time.gmtime(timestamp)           # NOTE: the "gmtime()" and "localtime()" are the method of "time_struct" Class, which returns the tuple of attributes from that Class. 😎

print("Date Time string: ", time.asctime(utc_time))

print("Date Time string: ", time.asctime(time.localtime(timestamp)))  # NOTE: If you don't provide an argument to the "asctime" function, 
                                                                      # the time returned by the localtime function will be used.

print("Date Time string: ", time.asctime())     # NOTE: If you don't provide an argument to the "asctime" function, the time returned by the localtime function will be used.



# NOTE: make Timestamp using mktime() : 

custom_timestamp = time.mktime((2020, 1, 25, 10, 35, 48, 0, 0, 0))      # NOTE: the values provided to "mktime" must be enclosed in "Tupele ()" 😎
print(custom_timestamp)                                                 # NOTE: the last 3 values are "tm_wday", "tm_yday", "tm_isdst" can be passed as 0, if those are unknown
                                                                        # and obviously those should be unknown to us, as we can't say any random year's random day's weekday or yearday 😅 

local_time = time.localtime(custom_timestamp)
utc_time = time.gmtime(custom_timestamp)
print(local_time, utc_time, sep='\n')

# NOTE: The second function called mktime converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch. 
# NOTE: In our example, we passed a tuple to it, which consists of the following values:

# NOTE: 2019 => tm_year
# NOTE: 11 => tm_mon
# NOTE: 4 => tm_mday
# NOTE: 14 => tm_hour
# NOTE: 53 => tm_min
# NOTE: 0 => tm_sec
# NOTE: 0 => tm_wday
# NOTE: 308 => tm_yday
# NOTE: 0 => tm_isdst



print(time.asctime(local_time))
print(time.asctime())                

print(time.asctime(utc_time))
