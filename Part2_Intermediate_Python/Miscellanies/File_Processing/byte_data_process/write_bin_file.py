from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i
    print(data)

try:
    bf = open('./bin_file/file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
print(data)
