
# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits, "elements exist in both list")


rows = ["A", "B", "C", "D", 'E', 'F', 'G', 'H']
lst = []

for i in range(1, 64+1):
    lst.append(i)
    if i % 2 != 0:
        lst.append("Black")
    else:
        lst.append("White")
    
print(lst)