
import sys
input = sys.stdin.readline
q = int(input())


texts = []
for _ in range(q):
    X = list(input().rstrip())
    X.insert(0, '')
    Y = list(input().rstrip())
    Y.insert(0, '')
    texts.append([X, Y])


for text in texts:
    X, Y = text[0], text[1]
    # print(X, Y)
    m = len(X)
    n = len(Y)
    # print(H, W)
    dps = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            # print(i, j)
            if Y[i] == X[j]:
                dps[i][j] = dps[i - 1][j - 1] + 1
            else:
                dps[i][j] = max(dps[i - 1][j], dps[i][j - 1])
    # print(dps)
    print(dps[n - 1][m - 1])
