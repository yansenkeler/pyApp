# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
# prime. There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many
# circular primes are there below one million?

import time
import tools


def is_circle_prime(c_num):
    for j in range(0, len(str(c_num))):
        index_num = int(str(c_num)[j:]+str(c_num)[:j])
        if not tools.is_prime(index_num):
            return False
    return True

startTime = time.time()
count = 0
for x in range(1, 1000000):
    if is_circle_prime(x):
        print(x)
        count += 1
print('total count: ', count)
# print(is_prime(9))
print('total time: ', time.time() - startTime, 'ms')
