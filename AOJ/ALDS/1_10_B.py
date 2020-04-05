N = int(input())

dimentions = []

for i in range(N):
    r, c = map(int, input().split())
    if i == 0:
        dimentions.append(r)
    dimentions.append(c)


# 行列の積の計算順序を決めたい
inf = float('inf')
dps = [[inf for _ in range(N)] for _ in range(N)]

for i in range(N):
    dps[i][i] = 0

# dps[i][j]を求めるにはdps[i][k]とdps[k + 1][j]が先に求まっている必要がある
for i in range(N - 1, -1, -1):
    # print(i)
    for j in range(i + 1, N):
        for k in range(i, j):
            dps[i][j] = min(dps[i][j],
                            dps[i][k] + dps[k + 1][j] + (dimentions[i] * dimentions[k + 1] * dimentions[j + 1]))
# print(dps)
print(dps[0][N - 1])
