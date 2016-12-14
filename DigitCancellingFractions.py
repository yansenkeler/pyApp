# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s. We shall consider
# fractions like, 30/50 = 3/5, to be trivial examples. There are exactly four non-trivial examples of this type of
# fraction, less than one in value, and containing two digits in the numerator and denominator. If the product of
# these four fractions is given in its lowest common terms, find the value of the denominator.
import time, re


# 得到2个数的最大公约数
def get_common_divisor(v1, v2):
    common_divisor = 1
    min_num = min(v1, v2)
    for x in range(1, min_num + 1):
        if v1 % x == 0 and v2 % x == 0 and x > common_divisor:
            common_divisor = x
    return common_divisor


# 是否是最简公约数
def is_simple(v1, v2):
    common_divisor = 1
    min_num = min(v1, v2)
    for x in range(1, min_num + 1):
        if v1 % x == 0 and v2 % x == 0 and x > common_divisor:
            common_divisor = x
    return common_divisor == 1


# 简化分数
def simply_fraction(fraction1):
    if re.match('^\d+/\d+$', fraction1):
        v1 = int(fraction1.split('/')[0])
        v2 = int(fraction1.split('/')[1])
        common_divisor = get_common_divisor(v1, v2)
        return str(int(v1 / common_divisor)) + '/' + str(int(v2 / common_divisor))
    else:
        return '0/0'


# 特殊方法简化分数
def special_simply_fraction(fraction2):
    change = False
    v1 = fraction2.split('/')[0]
    v2 = fraction2.split('/')[1]
    max_num = v1
    min_num = v2
    if len(v1) < len(v2):
        max_num = v2
        min_num = v1
        change = True
    for x in list(range(0, len(min_num))):
        index = max_num.find(min_num[x])
        if index >= 0:
            min_num = min_num.replace(min_num[x], '$', 1)
            max_num = max_num.replace(max_num[index], '$', 1)
    min_num = min_num.replace('$', '')
    max_num = max_num.replace('$', '')
    if change:
        return min_num + '/' + max_num
    else:
        return max_num + '/' + min_num


startTime = time.time()
for i in range(10, 100):
    for j in range(i + 1, 100):
        if str(i).find('0') == -1 and str(j).find('0') == -1:
            fraction = str(i) + '/' + str(j)
            f1 = simply_fraction(fraction)
            f2 = special_simply_fraction(fraction)
            if not is_simple(i, j):
                if f1 == f2:
                    print(i, j, f1, f2)


# print(simply_fraction('4/8'))
print('total spend time: ', round(time.time() - startTime, 5), 'ms')
