N, W = map(int, input().split())
inf = float('inf')

# 辺が繋がってる部分をdで表現する。infは繋がっていないとする
d = [[inf] * N for i in range(N)]
# 組み合わせの分dpsを作る。N=4なら、0000~1111で16必要
dps = [[-1] * N for i in range(1 << N)]

# print(dps)
for i in range(W):
    x, y, z = map(int, input().split())
    # x -> y はいけるということ
    d[x][y] = z


# 訪れた集合がs
# 今いる点がv
# 0に戻る最短経路を計算する
def rec(s, v, dp):
    # 0より大きかった場合、すでに数値がわかるのでreturn
    if dp[s][v] >= 0:
        return dp[s][v]
    # 全ての頂点を訪れている場合、1111で表現できる。
    # 1 << N でNビット左シフトする。
    # (s == (1 << N) - 1) の時は、最初の頂点以外が到達しているということ。0111111....
    if s == (1 << N) - 1 and v == 0:
        # 0以外の点に全て到達済みのdp[s] の、行き先のvに0を付与する
        dp[s][v] = 0
        return 0
    res = inf
    # iは0..N
    for i in range(N):
        # ここの意味がわからない
        # a >> b は bの右シフト・＃
        # (s>>i)
        if (s >> i & 1) == 0:
            # なんか更新してるけど、第二引数が謎。
            # s | (1 << i) はなに？
            # 今いる点。スタート地点。
            # d[v][i]は今いる点vから、iに行くときの重み。
            # そして、進んだ時のec(s | (1 << i), i, dp)にたす。　
            res = min(res, rec(s | (1 << i), i, dp) + d[v][i])
    dp[s][v] = res
    return res


ans = rec(0, 0, dps)
if ans == inf:
    print(-1)
else:
    print(ans)
