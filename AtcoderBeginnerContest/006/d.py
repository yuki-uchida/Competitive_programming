import bisect
# 1<= N <= 3*10^4
N = int(input())

nums = [int(input()) for _ in range(N)]

# numsを昇順に切り替える。
# その最小回数を割り出す
LIS = [nums[0]]
# dps = [0 for _ in range(N)]
# count = 0
for index, num in enumerate(nums):
    if index == 0:
        continue
    if LIS[-1] < num:
        LIS.append(num)
    else:
        LIS[bisect.bisect_left(LIS, num)] = num
        # LIS.insert(bisect.bisect_left(LIS, num), num)
# print(dps[-1])
print(N - len(LIS))
