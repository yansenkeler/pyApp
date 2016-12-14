# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For
# example, 2143 is a 4-digit pandigital and is also prime. What is the largest n-digit pandigital prime that exists?
import math, time, tools


# def validate_product(product):
#     if product.find('0') >= 0:
#         return False
#     for x in range(1, len(str(product))+1):
#         if product.count(str(x)) != 1:
#             return False
#     return True


def max_prime():
    max_p = 2
    for i in range(1234567, 7654322, 2):
        if tools.is_pan_digital(i, 1, 7) and tools.is_prime(i) and i > max_p:
            max_p = i
    return max_p

startTime = time.time()
print('result is ', max_prime())
print('total time: ', time.time() - startTime, 'ms')
