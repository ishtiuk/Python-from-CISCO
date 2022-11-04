
import calendar

cal = calendar.Calendar()


for date_wday in cal.monthdays2calendar(2022, 6):
    print(date_wday)


print(cal.monthdays2calendar(2022, 6))



# NOTE: this calendar modules "Calendar" Class's method named "monthdays2calendar()" contains a nested List including the ("date number", "week day") in a Tuple of each dates..... 🤩🤩🤩