import time
import itertools
import numpy
import tools


start = time.time()


def get_cubic_count(number):
    print(number)
    result = []
    for i in itertools.permutations(str(number), len(str(number))):
        n = int(''.join(list(i)))
        nn = numpy.power(n, 1/3)
        if tools.is_integer(nn):
            result.append(n)
        print(result)
    return len(set(result))

s = 200
flag = True
while flag:
    if get_cubic_count(s ** 3) == 5:
        flag = False
    s += 1


# print(get_cubic_count(41063625))
print(time.time() - start)
