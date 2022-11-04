from os import strerror


srcnm = input("Enter readfile name: ")
try:
    src = open(srcnm, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)


dstnm = input("Enter writefile name: ")
try:
    dst = open(dstnm, 'wb')
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)


total = 0
buffer = bytearray(65536)          # NOTE: it's a buffer with 64 kb space capacity... as we know from Engineering 1st semester EEF, 1024 bytes = 1 kb, so "1024 * 64 = 65536"
                                   # that's why we've used the number: "65536"

try:
    readin = src.readinto(buffer)
    print(readin)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written

        readin = src.readinto(buffer)

except IOError as ier:
    print("Cannot create the destination file: ", strerror(ier.errno))
    exit(ier.errno)

print(total, "byte(s) written successfully...")
src.close()
dst.close()
