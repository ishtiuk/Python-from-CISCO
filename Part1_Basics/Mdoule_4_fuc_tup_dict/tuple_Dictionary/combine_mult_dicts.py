
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'H', 'Patrick White': 'C'}
d3 = {'Smasher': 'C', 'Judy': 'D'}
d4 = {}

for item in (d1, d2, d3):
    print(item)
    d4.update(item)

print(d4)



colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)