n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.insert(0, 0)
inf = float('inf')
dps = [[inf for _ in range(n + 1)] for _ in range(m + 1)]
# for j in range(n + 1):
#     dps[0][j] = 0
for i in range(m + 1):
    dps[i][0] = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i == 1:
            dps[i][j] = j // coins[i]
            continue
        if j >= coins[i]:
            dps[i][j] = min(dps[i][j - coins[i]] + 1,
                            dps[i - 1][j - coins[i]] + 1,
                            dps[i - 1][j])
        else:
            dps[i][j] = dps[i - 1][j]
print(dps[m][n])
