
import itertools
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


K = int(input())

# 同じものが出てくるので、それを削減させる
# N^3の計算数が必要　1<=K<=200

# 1 + 3 + 3 + 1 = 8
permutaions = list(itertools.combinations_with_replacement(
    list(range(1, K + 1)), 3))
count = 0
for permutaion in permutaions:
    # print(permutaion, gcd(permutaion[0], permutaion[1], permutaion[2]))
    if permutaion[0] == permutaion[1] and permutaion[1] == permutaion[2]:
        count += gcd(permutaion[0], permutaion[1], permutaion[2])
    elif permutaion[0] != permutaion[1] and permutaion[1] != permutaion[2] and permutaion[0] != permutaion[2]:
        count += (6 * gcd(permutaion[0], permutaion[1], permutaion[2]))
    else:
        count += (3 * gcd(permutaion[0], permutaion[1], permutaion[2]))
print(count)
