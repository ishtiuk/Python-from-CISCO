from os import strerror

try:
    cnt = 0
    file = open('./file/text.txt', 'rt')
    content = file.read()

    for c in content:
        cnt += 1
    file.close()
    print(cnt)

except IOError as err:
    print("I/O error occured: ", strerror(err.errno))
