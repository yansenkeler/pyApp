# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
import math
import time


start_time = time.time()
total_sum = 0
for i in range(1, 1001):
    v = i ** i
    lt = str(int(v))[-10:]
    total_sum += int(lt)
    # print(i, total_sum)
print('result is ', str(total_sum)[-10:])
print('total time is ', time.time() - start_time, 'ms')
