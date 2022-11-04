
def the_digit_of_life(birthdate):
    birthdate = int(birthdate[:4]) + int(birthdate[4:6]) + int(birthdate[6:])

    while len(str(birthdate)) > 1:
        birthdate = sum(list(map(int, list(str(birthdate)))))

    return birthdate


usr_birth = input("Enter your birthday: YYYYMMDD: ")
print(the_digit_of_life(usr_birth))
