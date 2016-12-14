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


def nth_sum_prime(n):
    s = 0
    for i in range(1, n+1):
        s += nth_prime(i)
    return s


def is_triangle_number(num):
    delta = math.sqrt(1 + 8 * num)
    x1 = (-1 + delta) / 2
    return is_integer(x1)


def is_pentagon_number(number):
    delta = math.sqrt(1 + 24 * number)
    x1 = (1 + delta) / 6
    return is_integer(x1)


def is_hexagonal_number(number):
    delta = math.sqrt(1 + 8 * number)
    x1 = (1 + delta) / 4
    return is_integer(x1)


def is_integer(n):
    if str(n).strip('0').endswith('.'):
        return True
    return False


def get_all_approximate_numbers(number):
    result = []
    while number != 1:
        min_an = get_min_approximate_number(number)
        number /= min_an
        result.append(min_an)
    return result


def get_min_approximate_number(number):
    if is_prime(number):
        return int(number)
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return i
    return 1
