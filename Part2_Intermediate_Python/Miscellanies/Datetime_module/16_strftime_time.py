
import time

timestamp = 1572879180

local_time = time.localtime(timestamp)
utc_time = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", local_time))    # NOTE: time.strftime() requires second argument as "time.struct_time" Class Object, 
                                                         # if that isn't provided than it will convert current time wise... look at the second line🥴"
print(time.strftime("%Y/%m/%d %H:%M:%S"))



from datetime import time

time_obj = time(12, 5, 23)
print(time_obj)