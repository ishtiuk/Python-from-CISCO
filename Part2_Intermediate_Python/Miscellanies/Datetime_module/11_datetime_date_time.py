
from datetime import datetime


dt = datetime(2020, 5, 23, 6, 21)

print("Datetime: ", dt)
print("Date:", dt.date())
print("Time:", dt.time())



print("Datetime string: ", datetime.ctime(dt))

print(datetime.isoweekday(dt))
print(datetime.fromisoformat('2002-01-23'))

print(datetime.fromisoformat('2002-01-23 12:25:56.545444'))
print(datetime.fromisoformat('2002-01-23 12:25:56:545444'))