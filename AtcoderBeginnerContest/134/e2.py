import bisect
from collections import deque
N = int(input())
nums = deque([])

for i in range(N):
    num = int(input())
    if i == 0:
        nums.append(num)
    else:
        if nums[-1] < num:
            nums[-1] = num
        else:
            insert_index = bisect.bisect_left(nums, num)
            if insert_index == 0:
                nums.appendleft(num)
            else:
                nums[insert_index - 1] = num
#     print(nums)
# print(nums)
print(len(nums))
