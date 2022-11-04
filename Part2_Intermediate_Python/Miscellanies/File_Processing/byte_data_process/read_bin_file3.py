
from os import strerror

try:
    bf = open('./bin_file/file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# NOTE: the first five bytes of the file have been read by the code - the next five are still waiting to be processed.