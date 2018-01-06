from math import floor
val = 347991
total, level = 1, 1
while total < val:
    level += 2
    total = level*level
off = total-val
step = off % (level-1)
print(floor((level-1)/2 + abs((level/2)-step)))
