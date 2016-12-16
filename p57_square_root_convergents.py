# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
# is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
import time
from fractions import Fraction


def nth_fraction(n):
    c = 1
    s = Fraction(1, 2)
    while c < n:
        ts = Fraction(2, 1) + s
        s = Fraction(1, 1) / ts
        c += 1
    return Fraction(1, 1) + s


startTime = time.time()
count = 0
for i in range(1, 1000 + 1):
    expansion = nth_fraction(i)
    if len(str(expansion.numerator)) > len(str(expansion.denominator)):
        print(i, expansion)
        count += 1
print('result is ', count)
print('total time: ', time.time() - startTime, 'ms')
