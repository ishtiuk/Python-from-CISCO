
class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        self.h = "0" + str(self.__hour) if len(str(self.__hour)) == 1 else self.__hour
        self.m = "0" + str(self.__minute) if len(str(self.__minute)) == 1 else self.__minute
        self.s = "0" + str(self.__second) if len(str(self.__second)) == 1 else self.__second

        return f"{self.h}:{self.m}:{self.s}"

    def next_second(self):
        self.__second += 1

        if self.__second > 59:
            self.__minute += 1
            self.__second = 0
        if self.__minute > 59:
            self.__hour += 1
            self.__minute = 0
        if self.__hour > 23:
            self.__hour = 0


    def prev_second(self):
        self.__second -= 1

        if self.__second < 0:
            self.__minute -= 1
            self.__second = 59
        if self.__minute < 0:
            self.__hour -= 1
            self.__minute = 59
        if self.__hour < 0:
            self.__hour = 23



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)