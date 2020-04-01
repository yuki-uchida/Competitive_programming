# 疲労度の最小を出す

N, M = map(int, input().split())

distances = [0]
for _ in range(N):
    distances.append(int(input()))

weathers = [0]
for _ in range(M):
    weathers.append(int(input()))
# N個の都市と、N-1のその間の距離がある
# M日間の天気がある。
##
inf = float('inf')
dps = [[inf for _ in range(N + 1)]for _ in range(M + 1)]
# print(dps)

for i in range(M):
    dps[i][0] = 0
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if i < j:
            continue
        else:
            dps[i][j] = min(dps[i - 1][j - 1] + (weathers[i] * distances[j]),
                            dps[i - 1][j])

# print(dps)
print(dps[M][N])
