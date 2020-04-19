N, K = map(int, input().split())
# N = 何日あるか ,K = 先に渡される予定の数
schedules = [None for _ in range(N)]

for i in range(K):
    day, source = map(int, input().split())
    schedules[day - 1] = source
print(schedules)
dps = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    for j in range(3):
        if i == 0:
            if schedules[i]:
                if j == (schedules[i] - 1):
                    dps[i][j] = 1
            else:
                dps[i][j] = 1
        elif i == 1:
            if schedules[i]:
                if j == (schedules[i] - 1):
                    dps[i][j] = sum(dps[i - 1])
            else:
                dps[i][j] = sum(dps[i - 1])
        else:
            if schedules[i]:
                if j == (schedules[i] - 1):
                    # dps[i][j] = sum(dps[i - 1]) - \
                    #     (dps[i - 1][j] - dps[i - 2][j])
                    if dps[i - 1][j] > 0:
                        dps[i][j] = sum(dps[i - 1]) - \
                            (dps[i - 1][j] - dps[i - 2][j])
                    else:
                        dps[i][j] = sum(dps[i - 1])
            else:
                if dps[i - 1][j] > 0:
                    dps[i][j] = sum(dps[i - 1]) - \
                        (dps[i - 1][j] - dps[i - 2][j])
                else:
                    dps[i][j] = sum(dps[i - 1])
print(dps)
print(sum(dps[N - 1]) % 10000)
