# V=グラフの頂点の数
# E=辺の数
V, E = map(int, input().split())
inf = float('inf')
graphs = [[inf for _ in range(V)] for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    graphs[s][t] = d

# print(graphs)
# 横は集合
# 縦は向先

dps = [[-1 for _ in range(V)] for _ in range(1 << V)]
# これと一緒
# dps = [[-1 for _ in range(V**2)] for _ in range(V)]


def rec(s, v, dps):

    if dps[s][v] >= 0:
        return dps[s][v]

    if s == (1 << V) - 1 and v == 0:
        dps[s][v] = 0
        return 0
    res = inf
    # ゴールがV個
    for i in range(V):
        # 30 >> 0 & 1 == 0になる
        # 11110 >> 0 & 1 == 0 になる
        if (s >> i & 1) == 0:
            # s | (1 << i)
            # 00001 | 00110  => 00111
            # 00001 = 1 << 0
            # 00010 = 1 << 1
            # 00100 = 1 << 2
            # 01000 = 1 << 3
            res = min(res, rec(s | (1 << i), i, dps) + graphs[v][i])
    dps[s][v] = res
    return res


ans = rec(0, 0, dps)
if ans == inf:
    print(-1)
else:
    print(ans)
