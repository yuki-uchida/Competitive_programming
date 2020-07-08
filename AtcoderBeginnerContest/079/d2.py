H, W = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(10)]

nums = [0 for _ in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

ans = 0
for i in range(H):
    for num in list(map(int, input().split())):
        if num == -1:
            continue
        else:
            ans += costs[num][1]

print(ans)
