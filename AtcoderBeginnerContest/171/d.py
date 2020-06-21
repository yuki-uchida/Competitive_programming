import collections
N = int(input())
nums = list(map(int, input().split()))
Q = int(input())
nums_hash = collections.Counter(nums)
sum_point = sum(nums)
for _ in range(Q):
    # print(nums_hash)
    b, c = map(int, input().split())
    if b in nums_hash:
        sum_point = (sum_point - (b * nums_hash[b]) + (c * nums_hash[b]))
    print(sum_point)
    nums_hash[c] += nums_hash[b]
    nums_hash[b] = 0
