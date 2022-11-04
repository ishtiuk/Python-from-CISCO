
from os import strerror

try:
    bf = open('./bin_file/file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()
    print(data, len(data))

    bf = open('./bin_file/file.bin', 'rb')
    data = bytearray(bf.read(5))             # if we pass number in "read()" method, then it will read specified numbers of bytes... 😎
    bf.close()
    print(data, len(data))

except IOError as er:
    print("IO Error: ", strerror(er.errno))



# NOTE: Be careful - don't use this kind of read if you're not sure that the file's contents will fit the available memory.
# otherwise RAM will be filled up, and system malfunction will begin.... 😨