import time

a = time.time()
y = 1970 + round(a / 31556926)             # total second per year

m_sec = a % 31556926
m = round(m_sec / (60*60*24*29))

d_sec = m_sec % (60*60*24*30)
d = round(d_sec / 86400)

print(y, m, d)