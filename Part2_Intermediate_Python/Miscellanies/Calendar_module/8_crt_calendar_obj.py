import calendar


cal_obj = calendar.Calendar()    # NOTE: by-default value is in "Calendar()" init is 0 which stands for Monday.. but we can pass our customized parameter from 0-6 😎
                                 # NOTE: Hence, we have constants like: "calendar.MONDAY", "calendar.TUESDAY", "calendar.WEDNESDAY" etc which returns integer number by
                                 # conformig the rules of "datetime.datetime.weekday()" Mon = 0, Sun=6 
                                 # NOTE: so, we gonna use the "calendar.TUESDAY" like constants to ensure efficiency..... 😎

cal_obj = calendar.Calendar(calendar.SATURDAY)

for i in cal_obj.iterweekdays():
    print(i, end=' ')

print('\n')
cal_obj = calendar.Calendar(calendar.SUNDAY)


for i in cal_obj.iterweekdays():
    print(i, end=' ')


# Creating a Calendar object
# The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).

# The firstweekday parameter must be an integer between 0-6. For this purpose, we can use the already-known constants - look at the code in the editor.

# The program will output the following result:

# 6 0 1 2 3 4 5
# output

# The code example uses the Calendar class method named iterweekdays, which returns an iterator for week day numbers.

# The first value returned is always equal to the value of the firstweekday property. Because in our example the first value returned is 6, it means that the week starts on a Sunday.

