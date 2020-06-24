N, M = map(int, input().split())
inf = float('inf')
loads = [[inf for _ in range(N)] for _ in range(N)]
times = [[inf for _ in range(N)] for _ in range(N)]

for _ in range(M):
    s, t, d, time = map(int, input().split())
    loads[s - 1][t - 1] = d
    loads[t - 1][s - 1] = d
    times[s - 1][t - 1] = time
    times[t - 1][s - 1] = time
# print(loads)
# print(times)
# コスト・個数
dps = [[[inf, 0] for _ in range(N)] for _ in range(1 << N)]
dps[0][0] = [0, 1]
for S in range(1, 1 << N):
    for j in range(N):
        if S & (1 << j) == 0:
            continue
        prev_S = S - (1 << j)
        for k in range(N):
            # k->jに行くときの制限時間は超えてないか？
            if dps[prev_S][k][0] + loads[k][j] > times[k][j]:
                continue
            if dps[S][j][0] > dps[prev_S][k][0] + loads[k][j]:
                dps[S][j][0] = dps[prev_S][k][0] + loads[k][j]
                dps[S][j][1] = dps[prev_S][k][1]
            elif dps[S][j][0] == dps[prev_S][k][0] + loads[k][j]:
                dps[S][j][1] += dps[prev_S][k][1]
# print(dps)
# print(*dps[(1 << N) - 1][0])
if dps[(1 << N) - 1][0][0] == inf:
    print("IMPOSSIBLE")
else:
    print(*dps[(1 << N) - 1][0])
