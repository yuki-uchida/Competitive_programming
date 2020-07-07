N, M = map(int, input().split())
inf = float('inf')
roads = [[inf for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    roads[a - 1][b - 1] = t
    roads[b - 1][a - 1] = t

for i in range(N):
    roads[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])
# print(roads)
ans = inf
for i in range(N):
    ans = min(ans, max(roads[i]))
print(ans)
