# import sys

# input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:
        break
    weights = list(map(int, input().split()))
    dps = [[0 for _ in range(N)] for _ in range(N)]
    # can_out = [[False for _ in range(N)] for _ in range(N)]

    for w in range(2, N + 1):
        for i in range(N):
            j = i + w - 1
            if j >= N:
                continue
            if (dps[i + 1][j - 1] == w - 2 and abs(weights[i] - weights[j]) <= 1):
                dps[i][j] = w
            for k in range(i, j):
                dps[i][j] = max(dps[i][j], dps[i][k] + dps[k + 1][j])

    # print(dps)
    print(dps[0][N - 1])
