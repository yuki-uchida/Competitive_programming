n = int(input())

dimensions = []
for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        dimensions.append(a)
    dimensions.append(b)
inf = float('inf')
dps = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    dps[i][i] = 0
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        for k in range(i, j):
            dps[i][j] = min(dps[i][j],
                            dps[i][k] + dps[k + 1][j] + (dimensions[i] * dimensions[k + 1] * dimensions[j + 1]))
print(dps[0][n - 1])
