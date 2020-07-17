N, M, K = map(int, input().split())
loads = [list(map(int, input().split())) for _ in range(M)]
loads.sort(key=lambda x: x[2])

cities = [i for i in range(N)]
cost = 0


def root(node):
    if cities[node] == node:
        return node
    cities[node] = root(cities[node])
    return cities[node]


count = 0
for load in loads:
    a, b, c = load
    if count == N - K:
        break
    if not root(a - 1) == root(b - 1):
        cost += c
        count += 1
        cities[root(a - 1)] = root(b - 1)
print(cost)
