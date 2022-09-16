
lst = [45, 656, 54, 34, 443, 28, 4895, 566776]

for j in range(len(lst)):

    mini = j
    for i in range(j + 1, len(lst)):
        if lst[mini] > lst[i]:
            mini = i
    
    temp = lst[j]
    lst[j] = lst[mini]
    lst[mini] = temp

print(lst)