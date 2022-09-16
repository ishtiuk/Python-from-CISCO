
board = []

for i in range(8):
    rows = ["White" for i in range(8)]
    board.append(rows)

print(board)



# let's do the same thing in fully List Comprehension way 😁, 

board = [["White" for i in range(8)] for i in range(8)] 
print(board)