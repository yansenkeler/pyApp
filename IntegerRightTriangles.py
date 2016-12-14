# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
# solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50} For which value of p ≤ 1000, is the number of solutions
# maximised?
import math
import time


def solves_count(perimeter):
    count = 0
    for a in range(math.floor(perimeter / 3), math.ceil(perimeter / 2)):
        for b in range(math.floor(int((perimeter - a) / 2)), math.ceil(perimeter / 2)):
            c = perimeter - a - b
            if a * a == b * b + c * c:
                print(a, b, c)
                count += 1
    return count

startTime = time.time()
max_count = 0
max_d = 0
for d in range(1, 1000):
    tmp_count = solves_count(d)
    if tmp_count > max_count:
        max_count = tmp_count
        max_d = d
print('result is ', max_count, max_d)
# print('result is ', solves_count(840))
print('total time: ', time.time() - startTime, 'ms')