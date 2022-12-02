
def mysplit(strng):
    strng += ' '
    lst = []
    word = ''
    
    for i in strng:
        word += i
        word = word.strip()

        if i.isspace() and len(word) > 0:
            lst.append(word)
            word = ''
        # if i == ' ':
        #     lst.append(word.strip())
        #     word = ''

    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
