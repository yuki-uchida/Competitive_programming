N, K = map(int, input().split())
foods = [[] for _ in range(N)]
for _ in range(K):
    d = int(input())
    food = list(map(int, input().split()))
    for human in food:
        foods[human - 1].append(d)

count = 0
for food in foods:
    if len(food) == 0:
        count += 1

print(count)
