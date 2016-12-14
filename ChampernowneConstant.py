# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
import math, time


def nth_number(n):
    nth = 0
    count = 1
    while nth < n:
        nth += len(str(count))
        count += 1
    nth -= len(str(count - 1))
    return str(count - 1)[int(n) - nth - 1]


startTime = time.time()
s = 1
for z in range(0, 7):
    s *= int(nth_number(int(math.pow(10, z))))
print('result is ', s)
print('total time: ', time.time() - startTime, 'ms')