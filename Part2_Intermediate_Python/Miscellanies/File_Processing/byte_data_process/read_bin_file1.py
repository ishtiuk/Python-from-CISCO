
from os import strerror


try:
    data = bytearray(10)      # this is mutable ;), but the next files bytearray won't mutable... 🥴

    bf = open('./bin_file/file.bin', 'rb') 
    bf.readinto(data)
    bf.close()

    data = data[0:3] + bytearray(ord('a'))
    print(data)
    print(data)

    for i in data:
        print(hex(i), end='')

except IOError as ier:
    print("IO Error: ", strerror(ier.errno))
