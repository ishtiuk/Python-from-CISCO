import time

class date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.__str__()


    def __str__(self):
        rt = f"{self.year}-{self.month}-{self.day}"

        if len(str(self.month)) == 1:
            month = f'0{self.month}'
            rt = f"{self.year}-{month}-{self.day}"
        if len(str(self.day)) == 1:
            day = f'0{self.day}'
            rt = f"{self.year}-{month}-{day}"

        return rt

    def time_analyer(self):
        tm_stamp = time.time()
        y = 1970 + round(tm_stamp / 31556926)             # total second per year
        m_sec = tm_stamp % 31556926
        m = round(m_sec / (60*60*24*29))
        d_sec = m_sec % (60*60*24*30)
        d = round(d_sec / 86400)

        return y, m, d

    def today(self):
        y = self.time_analyer()[0]
        m = self.time_analyer()[1]
        d = self.time_analyer()[2]

        rt = f"{y}-{m}-{d}"

        if len(str(m)) == 1:
            m = f'0{m}'
            rt = f"{y}-{m}-{d}"
        if len(str(d)) == 1:
            d = f'0{d}'
            rt = f"{y}-{m}-{d}"

        return rt


obj = date(2005, 10, 12)
print(obj.today())
a = date(2002, 1, 2).today()
print(a)


