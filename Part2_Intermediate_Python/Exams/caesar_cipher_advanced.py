def encoding(text, gap):
    caesar_cipher = ''
    
    for c in text:
        if c.isalpha():
            if c.islower():
                if ord(c) <= ord('z') - gap:
                    caesar_cipher += chr(ord(c) + gap)
                else:
                    gap_left = ord('z') - ord(c)
                    gap_left = gap - gap_left
                    get_w = ord('a') + gap_left - 1

                    caesar_cipher += chr(get_w)
            if c.isupper():
                if ord(c) <= ord('Z') - gap:
                    caesar_cipher += chr(ord(c) + gap)
                else:
                    gap_left = ord('Z') - ord(c)
                    gap_left = gap - gap_left
                    get_w = ord('A') + gap_left - 1

                    caesar_cipher += chr(get_w)       
        else:
            caesar_cipher += c
            
    return caesar_cipher
    
    
txt = input('Enter your sms to encrypt: ')
try:
    gp = int(input('Enter the gappng num: '))

    if txt.isascii() and (gp >= 1 and gp <= 25):
        print(encoding(txt, gp))
    else:
        print("\nPlease make sure to enter a valid sms and a gapping number between 1 to 25..!")

except ValueError as err:
    print(err)


