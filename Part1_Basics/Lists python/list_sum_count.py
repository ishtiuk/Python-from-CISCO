# 1st way
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)



# 2nd way
my_list = my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)