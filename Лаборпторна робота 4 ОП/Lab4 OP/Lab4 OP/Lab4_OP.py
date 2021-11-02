from math import cos
from os import system
# знаходження точок перетину
range_start = -2
range_end = 2
start = 0
end = 0
start_found = False

for x in range(range_start, range_end):
    if round(1 / cos(x)) == round(3 - x**2):
        if not start_found:
            start = x
            start_found = True
        else:
            end = x

# знаходження площі
res = 0
for x in range(start, end):
    res += 3 - x**2 - 1 / cos(x)
print("first intersection:", start)
print("second intersection:", end)
print("square =", res, '~=', round(res, 3))
