
from os import strerror

try:
    cnt = 0
    file = open('./file/text.txt', 'r')
    line = file.readline()

    while line != '':
        for c in line:
            cnt += 1

        line = file.readline()
        
    file.close()
    print(cnt)

except IOError as err:
    print("I/O error: ", strerror(err.errno))


