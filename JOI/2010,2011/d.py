N = int(input())
nums = list(map(int, input().split()))
ans = nums.pop()

H = len(nums)
W = 20


dps = [[0 for _ in range(W + 1)] for _ in range(H)]
dps[0][nums[0]] = 1

for i in range(1, H):
    for j in range(W + 1):
        # print(i, j)
        if nums[i] == 0:
            dps[i][j] = dps[i - 1][j] * 2
        elif 0 <= j - nums[i] <= W and 0 <= j + nums[i] <= W:
            dps[i][j] = dps[i - 1][j - nums[i]] + dps[i - 1][j + nums[i]]
        elif j - nums[i] < 0:
            dps[i][j] = dps[i - 1][j + nums[i]]
        elif j + nums[i] > W:
            dps[i][j] = dps[i - 1][j - nums[i]]

# print(dps)
# print(len(dps))

# print(ans)
print(dps[H - 1][ans])
# ８つ目の時点でずれてる。
