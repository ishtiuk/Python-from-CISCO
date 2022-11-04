

from datetime import datetime

date1 = datetime(2020, 10, 25, 12, 19) 
date2 = datetime.now()

t_stamp_date1 = date1.timestamp()
t_stamp_now = date2.timestamp()

print(t_stamp_date1)
print(t_stamp_now)


print("time.struct_time class obj", date1.timetuple())

print("time.struct_time class obj", date2.timetuple())
