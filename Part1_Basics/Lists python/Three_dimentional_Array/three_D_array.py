
# Imagine that there are a hotel of 3 buildings. 
# 
# Each of the buildings have 15 floors 
# and each of the floors have 20 rooms.


rooms = [[[False for room in range(20)] for floor in range(15)] for buildings in range(3)]

# let's book the 2nd building's 10th floor room 14 ;)

rooms[1][9][13] = True
print(rooms[1][9])

# and release the 2nd room on the 5th floor located in the 1st building :D
rooms[0][4][1] = False
print(rooms[0][4])
print(not rooms[0][4][1])



# Check if there are any vacancies on the 15th floor of the third building:
total_vacancy = 0

for room_num in range(20):
    if not rooms[2][14][room_num]:
        total_vacancy += 1

print(f"Total empty rooms: {total_vacancy}")
