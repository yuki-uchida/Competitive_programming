N, M = map(int, input().split())
# 累積和用の配列 M個
memo = [[0] * (N + 1) for _ in range(M)]
cnt = [0] * M

# 累積和用の配列の更新
for i in range(1, N + 1):
    a = int(input()) - 1
    cnt[a] += 1
    memo[a][i] += 1
    for j in range(M):
        memo[j][i] += memo[j][i - 1]


cnt_Nuigurumi = [0] * (1 << M)
# 00 01 10 11 => 0->1でfor文回す
for bit in range(1 << M):
    for j in range(M):
        # 1bitずつ確認していく
        # 両方とも1の時に1。
        if bit & (1 << j):
            cnt_Nuigurumi[bit] += cnt[j]

# cnt_Nuigurumiは、ぬいぐるみの数のカウント
# 00 01 10 11 で 0 3 4 7

# print(memo)
# print(cnt)
# print(cnt_Nuigurumi)

inf = float('inf')
dp = [inf] * (1 << M)
dp[0] = 0
# print(dp)


for bit in range(1 << M):
    # 01みたいな感じ
    # 一桁ずつ確認していく
    for i in range(M):
        # 11の場合にはcontinue
        if bit & (1 << i):
            continue
        # 01 10 みたいな場合には11になる.
        bit_next = bit | (1 << i)
        R = cnt_Nuigurumi[bit_next]
        L = cnt_Nuigurumi[bit]
        # memo[i][R] - memo[i][L] で差分がわかる
        # これで切り替えなきゃいけない数がわかる。
        take = (R - L) - (memo[i][R] - memo[i][L])

        # bit_next は次の集合
        # bitは前の集合
        # dp[bit] + takeと、dp[bit_next]を比較して、小さい方を使う
        dp[bit_next] = min(dp[bit_next], dp[bit] + take)
print(dp)
print(dp[(1 << M) - 1])
