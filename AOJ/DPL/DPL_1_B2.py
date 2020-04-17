N, W = map(int, input().split())

values = [0]
weights = [0]

for _ in range(N):
    v, w = map(int, input().split())
    values.append(v)
    weights.append(w)

dps = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, W + 1):
        if j >= weights[i]:
            dps[i][j] = max(dps[i - 1][j], dps[i - 1]
                            [j - weights[i]] + values[i])
        else:
            dps[i][j] = max(dps[i - 1][j], dps[i][j - 1])
# print(dps)
print(dps[N][W])
