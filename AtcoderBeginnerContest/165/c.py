import itertools
N, M, Q = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(Q)]
# print(nums)
# 長さN
# 数字はMまで
num_permutations = list(
    map(list, itertools.combinations_with_replacement(list(range(1, M + 1)), N)))
# print(num_permutations)

maxcount = 0
for num_permutation in num_permutations:
    count = 0
    # print(num_permutation)
    for num in nums:
        # print(num)
        if num_permutation[num[1] - 1] - num_permutation[num[0] - 1] == num[2]:
            count += num[3]
            # print(num[3])
    maxcount = max(maxcount, count)
    # print(count)
    # print('=======================')
print(maxcount)
