import random
import numpy as np

# arr = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0], 
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3], 
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 2],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 0, 0]
# ]

# arr = np.array(arr)

# arr = np.array([[0 for i in range(9)] for j in range(9)])
arr = np.array([
    [4, 0, 8, 1, 0, 3, 0, 2, 0],
    [7, 0, 9, 0, 5, 6, 0, 3, 8],
    [0, 3, 2, 8, 4, 0, 7, 1, 6],
    [8, 9, 0, 3, 2, 4, 6, 0, 1],
    [2, 4, 0, 6, 0, 5, 8, 9, 7],
    [0, 5, 6, 7, 0, 0, 2, 0, 3],
    [3, 7, 5, 4, 0, 1, 9, 8, 2],
    [6, 8, 0, 9, 3, 2, 1, 0, 0],
    [0, 2, 1, 5, 0, 7, 3, 6, 0]
 ])
# print(arr)


def possible(row, column, number):
    global arr

    for c in range(9):
        if arr[row][c] == number:
            return False

    for r in range(9):
        if arr[r, column] == number:
            return False


    x0 = (row // 3) * 3
    y0 = (column // 3) * 3

    for i in range(3):
        for j in range(3):
            if arr[x0 + i][y0 + j] == number:
                return False

    return True


def solver():
    global arr
    
    for r in range(9):
        for c in range(9):   
            if arr[r][c] == 0:

                for n in range(1, 10):
                    if possible(r, c, n):
                        arr[r, c] = n
                        solver()
                            
                        arr[r, c] = 0
                return 
    print(f"Solved..!\n\n{arr}")


solver()


































def get_free_fields(arr):
    frees = []

    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if arr[r][c] == 0:
                frees.append((r, c))
                
    return frees


