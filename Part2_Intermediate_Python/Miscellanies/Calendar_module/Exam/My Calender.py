
from calendar import Calendar


class MyCalendar_Error(ValueError):
    def __init__(self, err):
        self.err = err
    def __str__(self):
        return self.err

class MyCalendar(Calendar):
    def __init__(self, firstweekday=0):
        super().__init__(firstweekday)


    def count_weekday_in_year(self, year, weekday=0):
        if year < 1 or year > 9999:
            raise MyCalendar_Error("[Year must be in range 0-9999]")
        elif weekday not in range(7):
            raise MyCalendar_Error("[Weekday must be in range 0-6]")

        all_week_lst = [self.monthdays2calendar(year, m) for m in range(1, 13)]
        total_occur = 0
        
        for m_wise in all_week_lst:
            for w_wise in m_wise:
                for d_wise in w_wise:
                    if d_wise[0] > 0 and d_wise[1] == weekday:
                        total_occur += 1

        return total_occur


obj = MyCalendar()

try:
    weekday_occured = obj.count_weekday_in_year(int(input("Enter Year: ")), int(input("Enter Weekday: ")))
    print(weekday_occured)
except MyCalendar_Error as er:
    print("Error: ", er)
except BaseException as berr:
    print("Base Error: ", berr)

