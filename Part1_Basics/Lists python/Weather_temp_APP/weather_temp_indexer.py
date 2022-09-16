# Multidimensional nature of lists: advanced applications
# Let's go deeper into the multidimensional nature of lists. To find any element of a two-dimensional list, you have to use two coordinates:

# a vertical one (row number)
# and a horizontal one (column number).
# Imagine that you develop a piece of software for an automatic weather station. The device records the air temperature on an hourly basis and does it throughout the month. This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

# First, you have to decide which data type would be adequate for this application. In this case, a float would be best, since this thermometer is able to measure the temperature with an accuracy of 0.1 ℃.

# Then you take an arbitrary decision that the rows will record the readings every hour on the hour (so the row will have 24 elements) and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days, so you need 31 rows). Here's the appropriate pair of comprehensions (h is for hour, d for day):


temps = [[0.0 for h in range(24)] for d in range(31)]
temps[1][11] = 22.5
temps[20][11] = 26.9
# The matrix is magically updated here.
#
# let's find out the average of noon temperature ;), as we know it'll be located on index no 11 ;)

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)





