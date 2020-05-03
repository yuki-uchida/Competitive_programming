N, M = map(int, input().split())

highs = list(map(int, input().split()))

loads = [set([]) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    loads[a - 1].add(b - 1)
    loads[b - 1].add(a - 1)
# print(highs)
# print(loads)
count = 0
for i, tower_loads in enumerate(loads):
    highest = True
    for load in tower_loads:
        if highs[i] <= highs[load]:
            highest = False
            break
    if highest:
        # print(i)
        count += 1
print(count)
