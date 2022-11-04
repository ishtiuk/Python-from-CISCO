from os import strerror

try:
    lcnt = wcnt = 0
    s = open('file/text.txt')
    lines = s.readlines(20)

    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for c in line:
                print(c, end='')
                wcnt += 1
        lines = s.readlines(20)

    s.close()
    print("\n\nCharacters in file:", wcnt)
    print("Lines in file:     ", lcnt)


except IOError as err:
    print("I/O error: ", strerror(err.errno))
