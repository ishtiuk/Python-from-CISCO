
# let's count the hot days during the month, hot day will be considered if it's temperature at midday is higher then 20.0 degree celsious. ;)

temps = [[0.0 for h in range(24)] for d in range(31)]

temps[0][11] = 19
temps[3][11] = 25
temps[10][11] = 26
temps[15][11] = 20.3


total_hot_days = 0

for day in temps:
    if day[11] > 20.0:
        total_hot_days += 1

print(f"Total hot days of this month: {total_hot_days} days.")
