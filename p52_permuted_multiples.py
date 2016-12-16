# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
#  order. Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
import time


def compare_two_number(n1, n2):
    l1 = list(str(n1))
    l2 = list(str(n2))
    list.sort(l1)
    list.sort(l2)
    return l1 == l2

start_time = time.time()
flag = True
a = 1
while flag:
    if compare_two_number(int(a), int(a*2)) and compare_two_number(int(a), int(a*3)) and compare_two_number(int(a), int(a*4)) and compare_two_number(int(a), int(a*5)) and compare_two_number(int(a), int(a*6)):
        flag = False
        print(a)
    a += 1
print('result is ', int(a-1), int((a-1)*2), int((a-1)*3), int((a-1)*4), int((a-1)*5), int((a-1)*6))
print('total time is ', time.time() - start_time, 'ms')
