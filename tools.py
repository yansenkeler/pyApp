import math


def is_prime(num):
    result = True
    if num <= 0 or num == 1 or num == 4:
        result = False
    elif num == 2 or num == 3:
        pass
    else:
        for i in range(2, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0:
                result = False
                break
    return result


# is start to end pandigital
def is_pan_digital(num, start, end):
    num_str = str(num)
    num_len = len(num_str)
    if num_len != end - start + 1:
        return False
    for i in range(start, end + 1):
        if num_str.count(str(i)) != 1:
            return False
    return True


def nth_prime(n):
    nth = 0
    number = 1
    while nth != n:
        if is_prime(number):
            nth += 1
        number += 1
    return number - 1
