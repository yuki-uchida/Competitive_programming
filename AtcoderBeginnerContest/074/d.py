
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if nums[i][j] > nums[i][k] + nums[k][j]:
                print(-1)
                exit()


max_cost = 0
for i in range(N):
    for j in range(i + 1, N):

        flag = True
        for k in range(N):
            if k == i or k == j:
                continue
            if nums[i][j] == nums[i][k] + nums[k][j]:
                flag = False
                break

        if flag:
            max_cost += nums[i][j]


print(max_cost)
