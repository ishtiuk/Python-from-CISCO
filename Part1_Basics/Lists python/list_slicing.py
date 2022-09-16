
# 
a = [5, 655, 4]

b = a              # here, list 'b' copies the list 'a's 'name' not 'contents', that means one's changes will effect another, and both 'a' and 'b's memory location is also same.

print(id(a), id(b))

b[0] = 756
print(a, b)         # as we can see both have been changed 😎




# but what if about coping list by 'slicing' or 'indexing', like below.....

c = a[:]      # here, the list 'c' copies the list 'a's 'contents', that means it just copies list contents, that means one's change wouldn't effect another 🐸😒d

print(id(c), id(a), id(b))

c[0] = 86978
print(c, a)



# print(c[0 : ])
# print(c[ : len(c)])
# print(c[0 : len(c)])



my_list = [10, 8, 6, 4, 2]
del my_list[0:3]
print(my_list)


del b[0]
print(b, a)