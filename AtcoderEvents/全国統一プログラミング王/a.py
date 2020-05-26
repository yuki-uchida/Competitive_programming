N = int(input())
area_resources = list(map(int, input().split()))

for i in range(1, N):
    area_resources[i] = area_resources[i - 1] + area_resources[i]
area_resources.insert(0, 0)
# print(area_resources)
for i in range(1, N + 1):
    max_cost = 0
    for j in range(i, N + 1):
        # print(j, j - i)
        max_cost = max(max_cost, area_resources[j] - area_resources[j - i])
    print(max_cost)
