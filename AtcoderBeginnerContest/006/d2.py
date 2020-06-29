import bisect
N = int(input())

# 1~Nの数字で作られていて、かぶることはない
nums = [0]

for _ in range(N):
    num = int(input())
    if nums[-1] < num:
        nums.append(num)
    else:
        nums[bisect.bisect_left(nums, num)] = num

print(N - (len(nums) - 1))
