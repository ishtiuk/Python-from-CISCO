
from datetime import datetime, time


my_date = datetime(2020, 11, 4, 14, 53, 00)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%m %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))

print('\nUsing "time.struct_time" Class')
print("Weekday:", my_date.timetuple().tm_wday + 1)
print("Day of the year:", my_date.timetuple().tm_yday)

# import time

