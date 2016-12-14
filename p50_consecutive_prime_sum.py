# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
import time
import tools


def get_prime_count(number):
    pass

start_time = time.time()
max_num = 0
# prime_index = 4
for j in range(1, 20):
    s_j = j
    x = 0
    tmp_index = 0
    while x < 1000000:
        prime_value = tools.nth_prime(j)
        x += prime_value
        if tools.is_prime(x) and x < 1000000:
            tmp_index = j
        j += 1
    print(s_j, tools.nth_sum_prime(tmp_index) - tools.nth_sum_prime(s_j - 1), tmp_index)
print('result is ', '')
print('total time is ', time.time() - start_time, 'ms')
