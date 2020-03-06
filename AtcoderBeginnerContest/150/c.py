import math
import itertools
N = int(input())
nums = []
for i in range(1, N + 1):
    nums.append(i)
permutaions_list = list(itertools.permutations(nums, N))
Ps = tuple(map(int, input().split()))
Qs = tuple(map(int, input().split()))

print(abs(permutaions_list.index(Ps) - permutaions_list.index(Qs)))
