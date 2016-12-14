import math
import time


# 判断等式是否满足Pandigital
def validate_product(product):
    if product.find('0') >= 0:
        return False
    for x in range(1, 10):
        if product.count(str(x)) != 1:
            # print(x, product.count(str(x)))
            return False
    return True


# 数字中如果有0或有重复的数字，不进行循环判断
def validate_num(num):
    if num.find('0') >= 0:
        return False
    for x in range(1, 10):
        if num.count(str(x)) > 1:
            return False
    return True


def validate_pro(num):
    for x in range(1, math.ceil(math.sqrt(num))):
        if num % x == 0:
            pro = str(x) + '*' + str(int(num / x)) + '=' + str(num)
            if len(pro) == 11 and validate_product(pro):
                print(pro)
                return True
    return False


startTime = time.time()
total = 0
i = 1000
while i < 100000:
    if validate_num(str(i)) and validate_pro(i):
        total += i
    i += 1
print('total : ', total)
print('total time: ', time.time() - startTime, 'ms')
