N, M, Q = map(int, input().split())
areas = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

for _ in range(M):
    left, right = map(int, input().split())
    areas[left][right] += 1
# print(areas)
for i in range(1, N + 2):
    for j in range(1, N + 2):
        areas[i][j] += areas[i][j - 1]
# print(areas)
for _ in range(Q):
    left, right = map(int, input().split())
    cost = 0
    for i in range(left, right + 1):
        cost += areas[i][right] - areas[i][left - 1]
    print(cost)
