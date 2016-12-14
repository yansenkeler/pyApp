# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
import math
import time
import tools


def get_prime_count(number):
    an = tools.get_all_approximate_numbers(number)
    an = set(an)
    count = 0
    for a in an:
        if tools.is_prime(a):
            count += 1
    return count

start_time = time.time()
flag = True
s_n = 646
while flag:
    if get_prime_count(s_n) == 4 and get_prime_count(s_n + 1) == 4 \
            and get_prime_count(s_n + 2) == 4 and get_prime_count(s_n + 3) == 4:
        print(s_n)
        flag = False
    s_n += 1

print('result is ', tools.get_all_approximate_numbers(660))
print('total time is ', time.time() - start_time, 'ms')
