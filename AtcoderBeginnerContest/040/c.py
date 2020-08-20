# 左にいくというケースは存在しないので、1or2の選択になる。
N = int(input())

highs = list(map(int, input().split()))

dps = [float("inf") for _ in range(N)]
dps[0] = 0
for i in range(1, N):
    if i == 1:
        dps[i] = abs(highs[i] - highs[0])
    else:
        dps[i] = min(dps[i - 1] + abs(highs[i] - highs[i - 1]), dps[i - 2] + abs(highs[i] - highs[i - 2]))

print(dps[N - 1])
