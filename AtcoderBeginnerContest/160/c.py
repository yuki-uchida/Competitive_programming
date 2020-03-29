K, N = map(int, input().split())
houses = list(map(int, input().split()))
# syaku_houses = []
# for i, num in enumerate(houses):
#     if i == 0:
#         syaku_houses.append(num)
#     else:
#         syaku_houses.append(num - houses[i - 1])
# print(syaku_houses)

# min_costs = []
# for house in syaku_houses:

# 右回りか左回りか？
for i in range(N - 1):
    houses.append(K + houses[i])

min_costs = []
for i in range(N):
    min_costs.append(houses[N - 1 + i] - houses[i])
print(min(min_costs))
