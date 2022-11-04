from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))


print('\n', end='')

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%Y/%B/%d %H:%M:%S"))
print(dt.strftime("%Y/%b/%d %H:%M:%S"))

# NOTE: "%B" uppercase for Long Month Name and "%b" lowercase for short Month NamE  ;)
print('\n')

print(dt.strftime("%Y/%A/%d %H:%M:%S"))
print(dt.strftime("%Y/%a/%d %H:%M:%S"))


# NOTE: "%A" uppercase for Long Day Name and "%a" lowercase for short Day Name ;)


print(datetime.ctime(dt))