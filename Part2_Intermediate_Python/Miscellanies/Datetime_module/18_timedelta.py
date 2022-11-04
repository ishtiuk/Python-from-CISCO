
from datetime import datetime, time, timedelta


d1 = datetime(2022, 6, 27, 23, 36)
d2 = datetime(2022, 5, 26, 22, 10)

delta = d1 - d2
print(delta)


delta2 = timedelta(weeks=2, days=2, hours=2)
print(delta2, delta2 * 2, sep='\n')