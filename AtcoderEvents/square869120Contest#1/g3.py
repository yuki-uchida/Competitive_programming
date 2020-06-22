N, M = map(int, input().split())
inf = float('inf')
bars = [[[inf, inf] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    s, t, d, time = map(int, input().split())
    bars[s - 1][t - 1] = [d, time]
    bars[t - 1][s - 1] = [d, time]
# print(bars)
# [最短コスト、個数]
dps = [[[inf, 0] for _ in range(N)] for _ in range(1 << N)]
# 1111の時を0,1とする
dps[(1 << N) - 1][0] = [0, 1]

# 0000を抜き、0001から調べていく
for s in range((1 << N) - 2, -1, -1):
    for j in range(N):
        # jが最後に到達したポイント。
        # kはどのポイントからjに行ったかを示している。
        # dps[prev][k] + bars[k][j][0]がコスト。これを街分出してminをとる。ただし制限時間は注意
        for k in range(N):
            if not (s >> k) & 1:
                # 0010 | 0001の場合、0011になる。
                # そして、最後の到達ポイントが1に値する
                if dps[s | 1 << k][k][0] + bars[j][k][0] <= bars[j][k][1]:
                    if dps[s][j][0] > dps[s | 1 << k][k][0] + bars[j][k][0]:
                        dps[s][j][0] = dps[s | 1 << k][k][0] + bars[j][k][0]
                        dps[s][j][1] = dps[s | 1 << k][k][1]
                    elif dps[s][j][0] == dps[s | 1 << k][k][0] + bars[j][k][0]:
                        dps[s][j][1] += dps[s | 1 << k][k][1]

# print(dps)
# 1111に到達していて、その中で、最後に0に到着したものを選択する
if dps[0][0][0] < inf:
    print(*dps[0][0])
else:
    print("IMPOSSIBLE")
