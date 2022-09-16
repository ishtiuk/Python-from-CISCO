
blocks = int(input("Enter number of blocks: "))
in_layer = 1
height = 0

while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1


print(height)