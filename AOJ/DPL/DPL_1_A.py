N, W = map(int, input().split())
values = list(map(int, input().split()))

dps = [[0 for _ in range(N + 1)] for _ in range(W + 1)]
dps[0] = [N + 1 for _ in range(N + 1)]
for i in range(W):
    for j in range(N + 1):
        if j > values[i]:
            dps[i + 1][j] = min(dps[i + 1][j - values[i]] + 1, dps[i][j])
        elif j == values[i]:
            dps[i + 1][j] = min(dps[i][j - values[i]] + 1, int(j // values[i]))
        else:
            dps[i + 1][j] = dps[i][j]
# print(dps)
print(dps[W][N])
