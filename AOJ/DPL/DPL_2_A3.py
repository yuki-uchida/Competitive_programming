V, E = map(int, input().split())
# bitDPで実装する。
# dps[s][p]は、すでに到達済みの集合sから、次のポイントpへ行くときの最短距離を示す。

inf = float('inf')
bars = [[inf for _ in range(V)] for _ in range(V)]

for _ in range(E):
    s, t, d = map(int, input().split())
    bars[s][t] = d


dps = [[-1 for _ in range(V)] for _ in range(1 << V)]
print(bars)
# print(dps)

#next_pointは最後に行った場所をメモするために使う
def bit_dp(sets, next_point, dps):
    if dps[sets][next_point] >= 0:
        return dps[sets][next_point]
    # 1110みたいに最終目的地以外到達済みかつ向かう点が0の時はreturnで返す
    if sets == ((1 << V) - 1) and next_point == 0:
        dps[sets][next_point] = 0
        return 0
    res = inf
    # 再帰的に進める。まずは1000,0100,0010,0001に移動する。
    for i in range(V):
        # 進む先iがすでに到達していないことを確認する
        if (sets >> i & 1) == 0:
            # 再帰的に進めるため、minで比較する
            res = min(res, bit_dp(sets | (1 << i), i, dps) + bars[next_point][i])
    dps[sets][next_point] = res
    return res


ans = bit_dp(0, 0, dps)
if ans == inf:
    print(-1)
else:
    print(ans)
print(dps)
