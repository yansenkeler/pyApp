# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence. What 12-digit number do you form by concatenating the three
# terms in this sequence?
import time
import tools


def compare_number(n1, n2):
    l1 = list(str(n1))
    l2 = list(str(n2))
    list.sort(l1)
    list.sort(l2)
    if l1 == l2:
        return True
    return False

start_time = time.time()
for i in range(1000, 3340 + 1):
    if tools.is_prime(i) and tools.is_prime(i + 3330) and tools.is_prime(i + 6660) and compare_number(i, i+3330) and compare_number(i, i+6660):
        print(i, i+3330, i+6660)
print('result is ', '')
print('total time is ', time.time() - start_time, 'ms')
