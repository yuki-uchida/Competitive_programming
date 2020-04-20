N, M = map(int, input().split())
distances = [int(input()) for _ in range(N)]
weathers = [int(input()) for _ in range(M)]

# 疲労=D*C なので、待機をうまく使って疲労度の最小値を求めたい
inf = float('inf')
dps = [[inf for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0:
            if j == 0:
                dps[i][j] = distances[i] * weathers[j]
            else:
                dps[i][j] = min(dps[i][j - 1], distances[i] * weathers[j])
        else:
            if i <= j:
                dps[i][j] = min(dps[i][j - 1], dps[i - 1]
                                [j - 1] + (distances[i] * weathers[j]))

print(dps[N - 1][M - 1])
