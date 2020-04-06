N = int(input())

nums = [int(input()) for _ in range(N)]
nums = nums + nums

dps = [[0] * (2 * N + 1) for i in range(2 * N + 1)]
ans = 0

for i in range(N):
    for j in range(2 * N - i):
        k = i + j
        if (N - i) % 2 == 1:
            dps[j][k] = max(dps[j + 1][k] + nums[j], dps[j][k - 1] + nums[k])
        else:
            if nums[k] > nums[j]:
                dps[j][k] = dps[j][k - 1]
            else:
                dps[j][k] = dps[j + 1][k]
        if i == N - 1:
            ans = max(ans, dps[j][k])

print(ans)
# print(dps)
