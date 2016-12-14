# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property. Let d1 be the 1st digit,
# d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
import time
import tools


def validate_special_property(number):
    for z in range(1, 8):
        jth_number = int(str(number)[z:z + 3])
        compare_prime = tools.nth_prime(z)
        if jth_number % compare_prime != 0:
            return False
    return True


def validate_nth_property(number, n):
    jth_number = int(str(number)[n:n + 3])
    compare_prime = tools.nth_prime(n)
    if jth_number % compare_prime != 0:
        return False
    return True


start_time = time.time()
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
total_sum = 0
for a in number_list[1:]:
    nl1 = number_list.copy()
    nl1.pop(number_list.index(a))
    for b in nl1:
        nl2 = nl1.copy()
        nl2.pop(nl1.index(b))
        for c in nl2:
            nl3 = nl2.copy()
            nl3.pop(nl2.index(c))
            for d in nl3:
                nl4 = nl3.copy()
                nl4.pop(nl3.index(d))
                for e in nl4:
                    nl5 = nl4.copy()
                    nl5.pop(nl4.index(e))
                    for f in nl5:
                        nl6 = nl5.copy()
                        nl6.pop(nl5.index(f))
                        for g in nl6:
                            nl7 = nl6.copy()
                            nl7.pop(nl6.index(g))
                            for h in nl7:
                                nl8 = nl7.copy()
                                nl8.pop(nl7.index(h))
                                for i in nl8:
                                    nl9 = nl8.copy()
                                    nl9.pop(nl8.index(i))
                                    for j in nl9:
                                        formed_number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j)
                                        if validate_special_property(int(formed_number)):
                                            print(formed_number)
                                            total_sum += int(formed_number)


print('result is ', total_sum)
print('total time is ', time.time() - start_time, 'ms')
