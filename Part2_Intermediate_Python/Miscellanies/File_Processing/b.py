
try:
    file = open('file/file.txt', 'r')

except IOError as exc:
    print(exc.errno)




