def find_next(avail, path, long_string):
    if not avail:
        if long_string[0:2] == long_string[-2:]:
            sum1 = 0
            for z in range(6):
                sum1 += int(long_string[z * 5:z * 5 + 4])
            print(long_string, ";  path ->", path, ";  sum =", sum1)
        return
    for i in avail:
        for j in p[i]:
            if long_string[-2:] == j[0:2]:
                new_list1 = avail[:]
                new_list1.remove(i)
                find_next(new_list1, path + " " + str(i), long_string + " " + j)
    return


new_list = []
p = [[] for a in range(9)]
f = [[] for b in range(9)]
n = 0
while True:
    n += 1
    f[3] = n * (n + 1) // 2
    if f[3] > 9999:
        break
    f[4] = n ** 2
    f[5] = n * (3 * n - 1) // 2
    f[6] = n * (2 * n - 1)
    f[7] = n * (5 * n - 3) // 2
    f[8] = n * (3 * n - 2)
    for r in range(3, 9):
        if 999 < f[r] <= 9999 and str(f[r])[2] != "0":
            p[r].append(str(f[r]))
print(p)
print(f)
for x in p[8]:
    find_next([3, 4, 5, 6, 7], "8", x)
