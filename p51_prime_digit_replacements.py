# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43,
#  53, 73, and 83, are all prime. By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113,
#  56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest
# prime with this property. Find the smallest prime which, by replacing part of the number (not necessarily adjacent
# digits) with the same digit, is part of an eight prime value family.
import time
import tools
import itertools
import re


def replace_operate_count(number, position):
    count = 0
    for i in range(0, 10):
        number_list = list(str(number))
        for index in position:
            number_list[index] = str(i)
        number_replace = int(''.join(number_list))
        if len(str(number_replace)) == len(str(number)):
            if tools.is_prime(number_replace):
                count += 1
    if count > 6:
        print(number, position, count)
    return count

start_time = time.time()
s_number = 56003
flag = True
while flag:
    if s_number % 5 != 0:
        for a in range(1, len(str(s_number))):
            position_list = list(range(0, len(str(s_number)) - 1))
            for b in itertools.combinations(position_list, a):
                c = replace_operate_count(s_number, list(b))
                if c == 8:
                    flag = False
                    print(s_number)
    s_number += 1
    # flag = False
# print('result is ', replace_operate_count(120303, [0, 2, 4]))
print('total time is ', time.time() - start_time, 'ms')
