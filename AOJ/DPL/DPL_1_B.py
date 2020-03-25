N, W = map(int, input().split())
weights = []
values = []
for _ in range(N):
    value, weight = map(int, input().split())
    weights.append(weight)
    values.append(value)

# 横軸：Wを超えないように選んだ時の価値の最大値(使える残りの重さとも言える)
# 縦軸：iまでの荷物を使った時の価値の最大値
dps = [[0 for _ in range(W + 1)] for _ in range(N + 1)]


# 荷物を0~i使った時の最小値をDPテーブルに保存しておく？
def napsack(weights, values, N, W, dps):
    for i in range(N):
        for j in range(W + 1):
            # print(i, j)
            if j >= weights[i]:
                dps[i + 1][j] = max(dps[i][j - weights[i]] +
                                    values[i], dps[i][j])
            else:
                dps[i + 1][j] = dps[i][j]


napsack(weights, values, N, W, dps)
# print(dps)
print(dps[N][W])
