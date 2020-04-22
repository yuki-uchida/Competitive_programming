N = int(input())

areas = [list(input()) for _ in range(5)]
dps = [[0 for _ in range(3)] for _ in range(N)]
# R = 0 B = 1 W = 2 # = 3
colors = ['R', 'B', 'W']
for i in range(N):
    for j in range(3):
        cost = 0
        for k in range(5):
            # print(i, j, k
            if colors[j] != areas[k][i]:
                cost += 1
            #     dps[i][j] = cost
        if i == 0:
            dps[i][j] = cost
        else:
            dps[i][j] = min(dps[i - 1][j - 1] + cost,
                            dps[i - 1][j - 2] + cost)
print(min(dps[N - 1]))
