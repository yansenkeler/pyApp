# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and
# twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math
import time
import tools


def is_satisfied_condition(num):
    a = 1
    nth_prime = tools.nth_prime(a)
    while nth_prime < num:
        d = num - nth_prime
        if d % 2 == 0 and tools.is_integer(math.sqrt(d / 2)):
            print(num, '=', nth_prime, '+2*', int(math.sqrt(d / 2)), '^2')
            return True
        a += 1
        nth_prime = tools.nth_prime(a)
    return False

start_time = time.time()
number = 33
flag = True
while flag:
    if not tools.is_prime(number):
        if not is_satisfied_condition(number):
            print(number)
            flag = False
    number += 2
print('result is ', '')
print('total time is ', time.time() - start_time, 'ms')