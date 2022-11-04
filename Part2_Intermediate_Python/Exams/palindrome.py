
def chcek_palindrome_str(strng):
    # we're gonna to avoid uppercase lowercase and spaces
    
    strng = strng.replace(' ', '').lower()
    reversed_strng = ''

    for c in strng:
        reversed_strng = c + reversed_strng

    if strng == reversed_strng:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


    # if strng == strng[::-1]:     # easiest shorcut hack ;)
    #     print("It's a palindrome")
    # else:
    #     print("It's not a palindrome")
        
        
chcek_palindrome_str(input("Enter string: "))