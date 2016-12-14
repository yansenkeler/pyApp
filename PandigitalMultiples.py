# Take the number 192 and multiply it by each of 1, 2, and 3:
#       192 × 1 = 192
#       192 × 2 = 384
#       192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
#  of 192 and (1,2,3) The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
# pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5). What is the largest 1 to 9
# pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n
# > 1?
import math, time


def validate_product(num):
    if str(num).find('0') >= 0 or len(str(num)) != 9:
        return False
    for x in range(1, 10):
        if str(num).count(str(x)) != 1:
            return False
    return True


def form_special_str(n, m):
    result = ''
    for i in range(1, m+1):
        result += str(n * i)
    return result

startTime = time.time()
max_num = 1
# 10000之后的和[1, 2]的乘积大于9位
for x in range(1, 10000):
    # [1, 2..., n]中n大于9的话不管多大的整数相乘都大于10位
    for y in range(2, 10):
        o = form_special_str(x, y)
        if validate_product(o):
            if int(o) > max_num:
                print(x, list(range(1, y+1)), o)
                max_num = int(o)

print('result is ', max_num)
print('total time: ', time.time() - startTime, 'ms')