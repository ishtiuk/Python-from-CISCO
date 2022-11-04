
from datetime import datetime


date = "2006/02/06"                          # NOTE: here seperator can be used anything like any alpha or any character: "2006n02n06" or "2006-02-06" anything, 
                                             # NOTE: but remember that the same seperator must be passed in "strptime()" method too... 😮‍💨😬
print(datetime.strptime(date, "%Y/%m/%d"))

time = "12:38:25"                            # NOTE: format can be anything "12*38-25" 🤣🤣
print(datetime.strptime(time, "%H:%M:%S"))  


dattime = "2006/02/06    12:38:25"
print(datetime.strptime(dattime, "%Y/%m/%d      %H:%M:%S"))




# NOTE: In the time module, you can find a function called strptime, which parses a string representing a time to a struct_time object. 
# Its use is analogous to the strptime method in the datetime class:

import time

print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


# Its result will be as follows:

# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, 