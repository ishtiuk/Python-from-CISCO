
lst = [1, 2, 3, 4]

for i in range(len(lst) // 2):
    temp = lst[i]
    lst[i] = lst[(len(lst) - (i + 1))] 
    lst[(len(lst) - (i + 1))] = temp

    # lst[i], lst[(len(lst) - (i + 1))] = lst[(len(lst) - (i + 1))], lst[i]          # same task


print(lst)



with open('file/file.txt', 'r+', encoding='cp1252') as file:
    print(file.write('dfdf\n\n'), file.readlines())

try:
    with open('file/fle.txt', 'x') as file:          # "x" mode for preventing duplicate creation and exclusive file creation.... ;)
        pass
except FileExistsError as ferr:
    print(ferr)



