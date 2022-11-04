from datetime import (date, datetime)

d = date.fromisoformat('2019-05-26')
print(d)


d = datetime.fromisoformat('2019-05-26')
print(d)                                      # NOTE: as always provides extra data about time ;)


d = datetime.fromisoformat('2019-05-26 02:47:58:578')
print(d)
print(" y- - m- d  h: M: S: microS")



# NOTE: When substituting the date, be sure to add 0 before a month or a day that is expressed by a number less than 10.

# NOTE: Note: The fromisoformat method has been available in Python since version 3.7.


# NOTE: what is ISO? read the following text carefully [from Google Search]  😅
# ISO 8601 represents date and time by starting with the year, followed by the month, the day, the hour, the minutes, seconds and milliseconds. For example, 
# NOTE: ""2020-07-10 15:00:00.000"", represents the 10th of July 2020 at 3 p.m. (in local time as there is no time zone offset specified—more on that below).Aug 13, 2020