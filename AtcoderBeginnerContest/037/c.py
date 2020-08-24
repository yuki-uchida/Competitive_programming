N, K = map(int, input().split())
nums = list(map(int, input().split()))


ans = sum(nums[0:K])
prev_total = sum(nums[0:K])
first_num = nums[0]
# print(ans, prev_total, first_num)
for i in range(K, N):
    prev_total -= first_num
    prev_total += nums[i]
    first_num = nums[i - (K - 1)]
    ans += prev_total
    # print(i, ans, prev_total, first_num)
# print(ans, prev_total, first_num)
print(ans)
