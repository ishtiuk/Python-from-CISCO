
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
while True:
    try:
        
            string = string + string
            print(len(string))
    except MemoryError:
        print('This is not funny!, Memory [RAM] has been fulled..! ')

