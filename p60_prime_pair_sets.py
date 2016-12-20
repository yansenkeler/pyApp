# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
#  primes, 792, represents the lowest sum for a set of four primes with this property. Find the lowest sum for a set
# of five primes for which any two primes concatenate to produce another prime.
from time import time
import itertools


def sieve(n):
    s = [False] * 3 + [True, False] * ((n - 2) // 2)
    p = [2]
    for i, j in enumerate(s):
        if j:
            p.append(i)
            for k in range(i * i, n, i):
                s[k] = False
    return p


a = set(sieve(100000000))
b = sieve(10000)
tic = time()


def concat_test(tup):
    if (tup[0] + tup[1]) % 3 == 0:
        return False
    tup = map(str, tup)
    m, q = tup
    if int(m + q) not in a:
        return False
    if int(q + m) not in a:
        return False
    return True


# initialise dict of primes, with each entry indicating the other primes it can be paired with
valid = {}
for p in b[1:]:
    valid[p] = set()

# fill dict
for c, d in itertools.combinations(b[1:], 2):
    if concat_test((c, d)):
        valid[c].add(d)
        valid[d].add(c)


def dfs(nodes, new_node, path=None):
    if path is None:
        path = []
    if all(n in nodes[new_node] for n in path):
        path += [new_node]
    else:
        return None
    if len(path) == 5:
        return path
    for n in sorted(list(nodes[new_node])):
        if n < new_node:
            continue
        if n not in path:
            continue_path = dfs(nodes, n, path[:])  # be very careful to use a copy of path here...
            if continue_path:
                return continue_path


for start in sorted(valid):
    res = dfs(valid, start, [])
    if res:
        print(res)

print("Time Elapsed: ", time() - tic)
