import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
n = int(input())
nums = list(map(int, input().split(" ")))
nums.sort(reverse=True)
q = int(input())
want_nums = list(map(int, input().split(" ")))

# 全部やるから再帰でやらないとダメ


def solve(i, want_num, nums=nums):
    if want_num == 0:
        return True
    if i >= n:
        return False
    else:
        res = solve(i + 1, want_num) or solve(i +
                                              1, want_num - nums[i])
        return res


for want_num in want_nums:
    if solve(0, want_num):
        print("yes")
    else:
        print("no")
