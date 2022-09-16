# let's find out the higest temperature of the month

temps_of_31_days = [[0.0 for h in range(24)] for d in range(31)]
temps_of_31_days[1][12] = 32
temps_of_31_days[3][12] = 25

highest_temp = -100
date_identify = 0

for day in temps_of_31_days:
    for temp in day:
        if temp > highest_temp:
            highest_temp = temp
            date_identify = temps_of_31_days.index(day) + 1

print(highest_temp, f"| date: {date_identify}")