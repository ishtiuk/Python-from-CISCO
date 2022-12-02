

# for ch in "b":
#     print(chr(ord(ch) + 1), end='')


def print_next_alpha(char):
    return chr(ord(char) - 32)

first = 'A'
for i in range(29):
    print(first, end=' ')
    first = print_next_alpha(first)
    

