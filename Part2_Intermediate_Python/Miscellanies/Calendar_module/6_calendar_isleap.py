
import calendar

print(calendar.isleap(2020))
print(calendar.isleap(2017))


print(calendar.leapdays(2010, 2020))       # the Last year's Leap days count won't be included, even the year won't. Just like the "range()" last element will be excluded.. 🥴
print(calendar.leapdays(2010, 2021))



print("Including Year 2012, 2016       :", calendar.leapdays(2010, 2020), "days")       
print("Including Year 2012, 2016, 2020 :", calendar.leapdays(2010, 2021), "days")