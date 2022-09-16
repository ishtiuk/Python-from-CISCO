
def print_alpha(prev = 'A'):
    print(prev, end=' ')

    for i in range(26):
        if ord(prev) >= ord('Z'):
            break

        prev = chr(ord(prev)  + 1)
        print(prev, end=' ')


user_alpha = input("Enter starting alpha: ").upper()
print_alpha(user_alpha)

