import math
import itertools
import re


# 是否为质数
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


# 第n个质数
def nth_prime(n):
    nth = 0
    number = 1
    while nth != n:
        if is_prime(number):
            nth += 1
        number += 1
    return number - 1


# 前n个质数之和
def nth_sum_prime(n):
    s = 0
    for i in range(1, n + 1):
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


# 是否是整数
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


def factorial(number):
    result = 1
    if number == 0:
        return 1
    for i in range(1, number + 1):
        result *= i
    return result


# a > b
def combination_count(a, b):
    return factorial(int(a)) / (factorial(int(b)) * factorial(int(a - b)))


# 是否为回文数
def is_palindrome(number):
    number_string = str(number)
    temp_string = number_string
    number_list = list(number_string)
    number_list.reverse()
    if temp_string == ''.join(number_list):
        return True
    return False


# 最小公倍数
def least_common_multiple(n1, n2):
    flag = True
    s_n = max(n1, n2)
    while flag:
        if s_n % n1 == 0 and s_n % n2 == 0:
            return s_n
        s_n += 1


# 最大公约数
def maximum_common_divisor(n1, n2):
    smaller = min(n1, n2)
    for i in range(smaller, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i


# 简化分数
def simply_fraction(fraction):
    if re.match('^\d+/\d+$', fraction):
        v1 = int(fraction.split('/')[0])
        v2 = int(fraction.split('/')[1])
        common_divisor = maximum_common_divisor(v1, v2)
        return str(int(v1 / common_divisor)) + '/' + str(int(v2 / common_divisor))
    else:
        return '0/0'


