from itertools import accumulate
N, M = map(int, input().split())

A = [[0 for _ in range(N + 1)]]
for i in range(N):
    text = list(input())
    rows = [0]
    for j, char in enumerate(text):
        if char == '#':
            rows.append(rows[j] + 1)
        else:
            rows.append(rows[j])
    A.append(rows)
B = [[0 for _ in range(M + 1)]]
for i in range(M):
    text = list(input())
    rows = [0]
    for j, char in enumerate(text):
        if char == '#':
            rows.append(rows[j] + 1)
        else:
            rows.append(rows[j])
    B.append(rows)
# print(A)
# print(B)
ans = False
for i in range(1, N - M + 2):
    for j in range(1, N + 2 - M):
        is_exist = True
        # print('=======', i, j)
        for k in range(1, M + 1):
            for l in range(1, M + 1):
                # print(k, l, B[k][l], A[i + k - 1][j + l - 1], A[i - 1][j], A[i][j - 1])
                if B[k][l] != (A[i + k - 1][j + l - 1] - A[i - 1][j]):
                    is_exist = False
        if is_exist:
            ans = is_exist
if ans:
    print('Yes')
else:
    print('No')
