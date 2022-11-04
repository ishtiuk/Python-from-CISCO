
# NOTE: The map() function applies the function passed by its first argument to all its second argument's elements, 
# and returns an iterator delivering all subsequent function results.


list_1 = [x for x in range(5)]
list_2 = list(map(lambda x : 2 ** x, list_1))

print(list_2)


for i in map(lambda x : x ** 2, list_2):
    print(i, end=' ')