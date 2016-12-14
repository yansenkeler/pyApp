# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math, time


def get_factorial(num):
    if num >= 2:
        sum_fact = 1
        for i in range(2, num + 1):
            sum_fact *= i
        return sum_fact
    else:
        return 1


def special_method(num):
    s = 0
    for i in range(0, len(str(num))):
        c_int = int(str(num)[i])
        s += get_factorial(c_int)
    if s == num:
        return num
    else:
        return 0


startTime = time.time()
total = 0
for i in range(10, 1000000):
    if special_method(i) == i:
        total += i
        print(i)
print('total is ', total)
# print(special_method(145))
print('total time: ', time.time() - startTime, 'ms')
