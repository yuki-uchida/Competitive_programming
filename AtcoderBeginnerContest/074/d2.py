N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
inf = float('inf')
dps = [[inf for _ in range(N)] for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            # costs[i][j]は最短経路でないといけない。
            if costs[i][j] > costs[i][k] + costs[k][j]:
                print(-1)
                exit()
max_cost = 0


for i in range(N):
    for j in range(i + 1, N):
        flag = True
        for k in range(N):
            if k == i or k == j:
                continue
            if costs[i][j] == costs[i][k] + costs[k][j]:
                flag = False
                break
        if flag:
            max_cost += costs[i][j]
print(max_cost)
