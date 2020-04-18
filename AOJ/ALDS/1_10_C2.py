q = int(input())
datasets = [list(input()) for _ in range(2 * q)]

for i in range(q):
    x, y = datasets[2 * i], datasets[(2 * i) + 1]
    dps = [[0 for _ in range(len(x) + 1)] for _ in range(len(y) + 1)]
    # print(y, x)
    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
            if y[i - 1] == x[j - 1]:
                dps[i][j] = max(dps[i - 1][j - 1] + 1, dps[i][j - 1])
            else:
                dps[i][j] = max(dps[i - 1][j], dps[i][j - 1])
    # print(dps)
    print(dps[len(y)][len(x)])
