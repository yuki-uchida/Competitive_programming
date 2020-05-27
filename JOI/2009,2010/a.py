import itertools
n, m = map(int, input().split())
distances = [int(input()) for _ in range(n - 1)]
# distances.insert(0, 0)
# for i in range(1, n):
#     distances[i] = distances[i] + distances[i - 1]
# print(distances)

distances = list(itertools.accumulate(distances))
distances.insert(0, 0)
# print(distances)
cost = 0
moves = [int(input()) for _ in range(m)]
now = 0
for move in moves:
    cost += abs(distances[now + move] - distances[now])
    cost %= 10**5
    now += move

print(cost)
