H, W = map(int, input().split())

change_costs = [list(map(int, input().split())) for _ in range(10)]
# change_costsは9*9のコスト


for k in range(10):
    for i in range(10):
        for j in range(10):
            # print(k, i, j)
            change_costs[i][j] = min(change_costs[i][j], change_costs[i][k] + change_costs[k][j])
# print(change_costs)
# nums = []
cost = 0
for _ in range(H):
    nums = list(map(int, input().split()))
    for num in nums:
        if num == -1:
            cost += 0
        else:
            cost += change_costs[num][1]
    # nums.append(list(map(int, input().split())))
print(cost)
