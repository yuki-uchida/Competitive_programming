import bisect
from collections import deque
N = int(input())
nums = [int(input()) for _ in range(N)]
# i<jで、 AiとAjが同じ色で塗られている場合、Ai < Ajが成り立つ.
# その際に、色の最小数をだす。
LIS = deque([nums[0]])
count = 0
for index, num in enumerate(nums):
    if index == 0:
        continue
    if num <= LIS[0]:
        LIS.appendleft(num)
    else:
        insert_index = bisect.bisect_left(LIS, num)
        LIS[insert_index - 1] = num
print(len(LIS))
