
# board = []
# for i in range(8):
#     rows = ["White" for x in range(8)]
#     board.append(rows)
blank = "-----"

board = [[blank for x in range(8)] for i in range(8)]
board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"
# now let's make a visual look of a Chess Board 😎😁
print("     A        B        C        D        E        F        G        H")


length = len(board)
for li in range(len(board)):
    print(length, board[li])
    length -= 1
print("     A        B        C        D        E        F        G        H")
print("{:>40s}".format("Chess Board"))



# now let's place some pieces to the board 😁
# let's place "KNIGHT" to "C5" 😎

board[3][2] = "KNIGHT"

print("    A        B        C        D        E        F        G        H")
for row in board:
    print(row)
print()

# let's place "PAWN" to "H3" 😎

board[5][7] = "PAWN"

print("    A        B        C        D        E        F        G        H")
for row in board:
    print(row)
