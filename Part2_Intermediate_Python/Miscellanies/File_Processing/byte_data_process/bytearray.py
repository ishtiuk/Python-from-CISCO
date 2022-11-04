data = bytearray(10)
print(data)


for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
