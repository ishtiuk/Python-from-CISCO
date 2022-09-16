
c0 = int(input("Enter: "))
steps = 0


    
while c0 > 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        
    else:
        c0 = 3 * c0 + 1
        
    print(c0)
    steps += 1
    
print("steps = ", steps)




# num = "0165031806510"
# num = list(num)

# for digit in num:
#     if digit == "0":
#         num[num.index(digit)] = "x"

# print(''.join(num))