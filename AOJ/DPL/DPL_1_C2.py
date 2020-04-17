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
        if i == 1:
            if j >= weights[i]:
                dps[i][j] = values[i] * (j // weights[i])
        else:
            if j >= weights[i]:
                dps[i][j] = max(dps[i][j - (weights[i])] +
                                values[i], dps[i - 1][j])
                # for k in range(j // weights[i] + 1):
                # dps[i][j] = max(dps[i][j - (weights[i] * k)] + (values[i] * k),
                #                 dps[i][j])
                dps[i][j] = max(dps[i][j], dps[i][j - 1])
            else:
                dps[i][j] = max(dps[i][j - 1], dps[i - 1][j])
print(dps[N][W])
