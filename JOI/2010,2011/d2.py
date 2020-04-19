N = int(input())  # N <= 100
nums = list(map(int, input().split()))
ans = nums[-1]
nums = nums[0:N - 1]
# print(nums, ans)
# 計算の途中で20を超えない.かつ負にならない


dps = [[0 for _ in range(21)] for _ in range(N - 1)]
# print(dps)
for j in range(21):
    if nums[0] == j:
        dps[0][j] = 1
# print(dps)

for i in range(1, N - 1):
    for j in range(21):
        count = 0
        if j - nums[i] >= 0:
            count += dps[i - 1][j - nums[i]]
        if j + nums[i] <= 20:
            count += dps[i - 1][j + nums[i]]
        dps[i][j] = count
print(dps[N - 2][ans])
