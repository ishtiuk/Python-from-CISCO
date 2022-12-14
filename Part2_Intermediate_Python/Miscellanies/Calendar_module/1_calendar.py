
import calendar

print(calendar.MONDAY)
print(calendar.TUESDAY)
print(calendar.WEDNESDAY)
print(calendar.THURSDAY)
print(calendar.FRIDAY)
print(calendar.SATURDAY)
print(calendar.SUNDAY)


# Introduction to the calendar module
# In addition to the datetime and time modules, the Python standard library provides a module called calendar which, as the name suggests, offers calendar-related functions.

# One of them is of course displaying the calendar. It's important that the days of the week are displayed from Monday to Sunday, and each day of the week has its representation
#  in the form of an integer:

# Day of the week	Integer value	Constant
# Monday	0	calendar.MONDAY
# Tuesday	1	calendar.TUESDAY
# Wednesday	2	calendar.WEDNESDAY
# Thursday	3	calendar.THURSDAY
# Friday	4	calendar.FRIDAY
# Saturday	5	calendar.SATURDAY
# Sunday	6	calendar.SUNDAY
# The table above shows the representation of the days of the week in the calendar module. The first day of the week (Monday) is represented by the value "0" and the "calendar.MONDAY"
# constant, while the last day of the week (Sunday) is represented by the value 6 and the calendar.SUNDAY constant.

# A snake and a calendar

# For months, integer values are indexed from 1, i.e., January is represented by 1, and December by 12. Unfortunately, there aren't constants that express the months.

# The above information will be useful to you when working with the calendar module in this part of the course, but first let's start with some simple calendar examples.

