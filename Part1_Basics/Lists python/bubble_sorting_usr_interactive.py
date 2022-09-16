
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))                  # now, here we've used the "float" function to handle both float or integer numbers.. so, users can also enter float numbers too..
    my_list.append(val)                                           # like:  12.0, 12.33, 12.45, 45, 24, 56 etc.

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
