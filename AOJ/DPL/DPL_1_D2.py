import bisect
n = int(input())
nums = [int(input()) for _ in range(n)]

LIS = [nums[0]]

for num in nums:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        LIS[bisect.bisect_left(LIS, num)] = num

print(len(LIS))
