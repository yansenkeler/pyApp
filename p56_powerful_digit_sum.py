# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one
# followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
import time
import math


def digital_sum(number):
    result = 0
    for a in list(str(number)):
        result += int(a)
    return result


startTime = time.time()
max_digital_sum = 0
ti = 0
ji = 0
for i in range(1, 100):
    for j in range(1, 100):
        n = i ** j
        ds = digital_sum(n)
        if ds > max_digital_sum:
            max_digital_sum = ds
            ti = i
            tj = j

print('result is ', max_digital_sum, ti, ji)
print('total time: ', time.time() - startTime, 'ms')
