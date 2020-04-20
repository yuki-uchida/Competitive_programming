from itertools import combinations
N, K = map(int, input().split())
nums = [0 for _ in range(N + 1)]
for i in range(N + 1):
    if i == 0:
        nums[i] = 0
    else:
        nums[i] = nums[i - 1] + i
# print(nums)
if N + 1 == K:
    print(1)
else:
    count = 1
    for i in range(K, N + 1):
        # iは組み合わせに使うかず
        # 2,3,4
        min_nums = nums[i - 1]
        max_nums = nums[N] - nums[N - i]
        count += max_nums - min_nums + 1

    print(count % (10**9 + 7))
