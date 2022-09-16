
# 1st way

# lst = ['z', 'y', 'x', 'w', "v"]
lst = [10, 1, 8, 3, 5]
j = 1

for i in range(len(lst) // 2):
    temp = lst[i]
    lst[i] = lst[-j]
    lst[-j] = temp
    j += 1

print(lst)
print('\n\n\n')



# 2nd way

lst = [10, 1, 8, 3, 5]

for i in range(len(lst) // 2):
    lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]

print(lst)
