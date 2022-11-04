
import time

timestamp = time.time()

utc_gmt_t = time.gmtime(timestamp)
local_time = time.localtime(timestamp)


print("Year:", utc_gmt_t.tm_yday)
print("Month:", utc_gmt_t.tm_mon)
print("Day:", utc_gmt_t.tm_mday)
print("Hour:", utc_gmt_t.tm_hour)
print("Minute:", utc_gmt_t.tm_min)
print("Second:", utc_gmt_t.tm_sec)
print("Week Day:", utc_gmt_t.tm_wday)         # weekday 0 is "Mon" and 6 is "Sun", just like the "datetime.weekday()" ;)
print("Year Day:", utc_gmt_t.tm_yday)


print("UTC or GMT Time: ", utc_gmt_t)

print("Locat Time: ", local_time)         # NOTE: notice here, the "tm_hour" of "locat_time" is 6 hours greater than the "utc_gmt_t", 
                                          # because  BST — Bangladesh Standard Time is "UTC/GMT +6 hours"    [UTC and GMT coordinates are the same]



# NOTE: above mentioned tow methods are very usefull because they are providing lots of attributes about the Date and Time,
# which can be handy to calculate any date or time 😎😎