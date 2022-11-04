
from datetime import date, datetime

d = date(2019, 11, 4)
print(d.weekday())

d = datetime(2019, 11, 4)
print(d.weekday())

# NOTE: One of the more helpful methods that makes working with dates easier is the method called weekday. It returns the day of the week as an integer,
# where 0 is Monday and 6 is Sunday. Run the code in the editor.

# Result:
# 0

from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())

d = datetime(2019, 11, 4)
print(d.isoweekday())

# NOTE: The date class has a similar working method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday:

# Result:
# 1

# As you can see, for the same date we get a different integer, but expressing the same day of the week. 
# The integer returned by the isodayweek method follows the ISO 85601 specification.

print(date.today().strftime('%Y-%m-%d'))

