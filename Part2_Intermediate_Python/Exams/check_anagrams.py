
def check_anagrams(text1, text2):
    anagram = True
    
    for c in text1:
        if c not in text2:
            anagram = False
            
    if anagram:
        return "Anagrams"
    else:
        return "Not Anagrams!"
        

t1 = input("Enter text1: ").lower()
t2 = input("Enter text2: ").lower()

print(check_anagrams(t1, t2))