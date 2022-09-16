
lst = [5, 6, 4, 1, 65, 54, 90, 33]

for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp

print(lst)