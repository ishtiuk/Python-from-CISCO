


my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:                                                 #  notice here, we've used "While" loop instead of a "for" loop 🙄, which we used during our first sorting algo learning time
    swapped = False  # no swaps so far                         # Hence, both are same "while" or "for", both method follows "nested loop" principal
    for i in range(len(my_list) - 1):                          # and Both method's   Time Complexity = O (n ^ 2)    😎😎
         if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            print(swapped)
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)



my_list = [8, 10, 6, 2, 4]

for i in range(len(my_list)):
    for j in range(len(my_list) - 1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)

