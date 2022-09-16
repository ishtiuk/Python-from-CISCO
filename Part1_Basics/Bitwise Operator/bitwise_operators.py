

# the "Bitwise Operators" works with bits, firstly it converts number to binary bits, then runs operator bitwisely according to the "bitwise_Operator.jpg" image's rules......
# 1. Ampersand " & " 
# 2. Bar " | "
# 3. Caret " ^ "
# 4. Tilde " ~ "

print(25 | 30) 

print(25 & 30)

print(25 ^ 30)

print( ~ 16)

x, y = 15, 25

x = x & y
print(x)	          # x &= y             # just like " a = a + b , maybe wriiten like this:  "a += b"  "

x = x | y
print(x)	          # x |= y

x = x ^ y	          # x ^= y
print(x)

# n = int(input(": "))
# decilcal = 0
# i = 0

# while n > 0:
#     lst_num = n % 10
#     decilcal += (lst_num * (2 ** i))
#     n //= 10
#     i += 1

# print(decilcal)

