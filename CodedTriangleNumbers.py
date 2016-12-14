# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11
# + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word. Using
# words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English
#  words, how many are triangle words?
import math, time


def is_triangle_number(num):
    delta = math.sqrt(1 + 8 * num)
    x1 = (-1 + delta) / 2
    if str(x1).rstrip('0').endswith('.'):
        print(int(x1))
        return True
    return False


def calculate_word_value(word):
    total_sum = 0
    for i in range(0, len(word)):
        total_sum += ord(word[i]) - 64
    return total_sum


startTime = time.time()
count = 0
fo = open('p042_words.txt', 'r+')
data = fo.read()
data = data[1:-1]
data_list = data.split('","')
for x in data_list:
    if is_triangle_number(calculate_word_value(x)):
        print(x)
        count += 1

print('result is ', count)

print('total time: ', time.time() - startTime, 'ms')
