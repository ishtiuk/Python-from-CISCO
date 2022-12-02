
def IBAN_validator(IBAN):
    ISO_3166_alpha2 = []   # this gonna be loaded from CSV  ;)
    IBAN = IBAN.replace(' ', '').upper()
    

    if not IBAN.isalnum():
        return "Sorry entered IBAN is invalid! It doesn't contain alphanumeric."
    elif len(IBAN) < 15:
        return "Ops too short IBAN"
    elif len(IBAN) > 31:
        return "Ops too long IBAN"

    IBAN = IBAN[4 : ] + IBAN[0 : 4]
    IBAN_valid = ''

    for char in IBAN:
        if char.isdigit():
            IBAN_valid += char
        else:
            IBAN_valid += str(10 + ord(char.upper()) - ord('A'))
        
    if int(IBAN_valid) % 97 == 1:
        return "IBAN validation is passed..."
    else:
        return "IBAN validation isn't passed..."
    



iban = input("Enter your IBAN for validation: ")
print(IBAN_validator(iban))
