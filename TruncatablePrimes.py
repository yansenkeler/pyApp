# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3. Find the sum of the only eleven primes that are both truncatable from left to right and right
#  to left. NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import math, time, tools


def is_left_prime(num):
    for j in range(0, len(str(num))):
        n = int(str(num)[j:])
        if not tools.is_prime(n):
            return False
    return True


def is_right_prime(num):
    for j in range(1, len(str(num))):
        right_index = -j
        n = int(str(num)[:right_index])
        if not tools.is_prime(n):
            return False
    return True

start_time = time.time()
total_sum = 0
for i in range(10, 1000000):
    if is_left_prime(i) and is_right_prime(i):
        print(i)
        total_sum += i
print('result is ', total_sum)
print('total time is ', time.time() - start_time, 'ms')
