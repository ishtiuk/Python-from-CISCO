from datetime import date
from datetime import datetime

my_date = date(2019, 11, 4)            # NOTE: 'date' cls only includes date data: like Year-month-day
print(my_date)


my_date = datetime(2019, 11, 4)       # NOTE: 'datetime' cls only includes date data and time data also: like Year-month-day hour:minute:second   😎
print(my_date)


from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
