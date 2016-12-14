# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
import math, time


def is_palindromes(num):
    l = list(str(num))
    l.reverse()
    reversed_num = int(''.join(l))
    if num == reversed_num:
        return True
    return False


def decimal_to_binary(dec):
    return int(str(bin(dec))[2:])

startTime = time.time()
sum_num = 0
for y in range(1, 1000000):
    if is_palindromes(y) and is_palindromes(decimal_to_binary(y)):
        print(y, decimal_to_binary(y))
        sum_num += y
print('total sum is: ', sum_num)
# print(is_palindromes(decimal_to_binary(585)))
print('total time: ', time.time() - startTime, 'ms')