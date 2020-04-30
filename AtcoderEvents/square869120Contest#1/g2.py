# 建物がN個
# 道路がM本
N, M = map(int, input().split())

inf = float('inf')
loads = [[(inf, -1) for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s, t, d, time = map(int, input().split())
    loads[s - 1][t - 1] = loads[t - 1][s - 1] = (d, time)
dps = [[[inf, 1] for _ in range(N)] for _ in range(1 << N)]
dps[(1 << N) - 1][0] = [0, 1]


for s in range((1 << N) - 2, -1, -1):
    for j in range(N):
        for k in range(N):
            if not (s >> k) & 1:
                if dps[s | 1 << k][k][0] + loads[j][k][0] <= loads[j][k][1]:
                    if dps[s][j][0] > dps[s | 1 << k][k][0] + loads[j][k][0]:
                        dps[s][j][0] = dps[s | 1 << k][k][0] + loads[j][k][0]
                        dps[s][j][1] = dps[s | 1 << k][k][1]
                    elif dps[s][j][0] == dps[s | 1 << k][k][0] + loads[j][k][0]:
                        dps[s][j][1] += dps[s | 1 << k][k][1]

if dps[0][0][0] < inf:
    print(*dps[0][0])
else:
    print("IMPOSSIBLE")
