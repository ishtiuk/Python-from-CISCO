from datetime import datetime
from datetime import date


class DateError(ValueError):
    def __str__(self):
        return "Follow this Date format: YYYY-MM-DD\nNOTE: [You must use ISO format '-' seperator]"
    

def counter(date_of_b):
    if date_of_b.count('-') >= 2:
        date_of_b = datetime.strptime(date_of_b, '%Y-%m-%d')
    else:
        raise DateError

    today = datetime.now()
    age = today - date_of_b
    print("\nYour current age: ", age.days // 365, "Years")

usr = input("Enter Date Of Birth in YYYY-MM-DD format\n: ").strip()

try:
    counter(usr)
except DateError as er:
    print("\nError:", er)
except BaseException as er:
    print("\nError:", er)

