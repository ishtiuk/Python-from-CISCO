
class WeekDayError(Exception):
    pass
	

class Weeker:
    week_lst = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day in self.week_lst:
            self.__day = day
        else:
            raise WeekDayError


    def __str__(self):
        return self.__day


    def add_days(self, n):
        days_left = len(self.week_lst) - self.week_lst.index(self.__day)        # this can be done like:  "(self.week_lst.index(self.__day) + 1)", for more transparency... 🤩                                                   # this can be done like: "day = calc % len(self.week_lst)  - 1", for more transparency... 🤩
        day = (n - days_left) % len(self.week_lst)                                         

        self.__day = self.week_lst[day]


    def subtract_days(self, n):
        days_left = 7 - (7 - self.week_lst.index(self.__day))                  # here, 7 has been used instead of "len(self.week_lst)" for little bit simplicity.. 😅🥱
        day = (n - days_left) % 7                            

        self.__day = self.week_lst[-day]



try:
    weekday = Weeker('Tue')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(3)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")



