N, M = map(int, input().split())
# バス停の数がN
# 路線の数がM
inf = float('inf')
towns = [[inf for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    towns[a - 1][b - 1] = cost
    towns[b - 1][a - 1] = cost

for i in range(N):
    towns[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            towns[i][j] = min(towns[i][j], towns[i][k] + towns[k][j])
min_cost = inf
for i in range(N):
    min_cost = min(min_cost, max(towns[i]))
print(min_cost)
