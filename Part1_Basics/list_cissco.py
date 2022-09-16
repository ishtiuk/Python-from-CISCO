
lst = [5, 65, 767, 44, 34, 55, 676, 454]

print(lst)

del  lst[0]

lst.pop(0)
print(lst)

lst.remove(676)
print(lst)


lst.insert(2, 111100111)
print(lst)

lst.insert(11, 5545454)        # if we enter the location more than the existing indexes of the list, it will not throw any Error, 
print(lst)                     # and it will add the "element here: 5545454" at the end of list.



# let's make a ascending array using "for" loop , like fun 😁😎
my_lst = []

for i in range(5):
    my_lst.append(i + 1)


print(my_lst)


# let's make a descending array using "for" loop , like fun 😁😎
my_lst = []

for i in range(5):
    my_lst.insert(0, i + 1)

print(my_lst)



