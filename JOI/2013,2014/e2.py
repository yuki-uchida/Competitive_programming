from collections import deque
N, K = map(int, input().split())
taxies = [list(map(int, input().split())) for _ in range(N)]
graphs = [[] for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    # print(graphs, a, b)
    graphs[a - 1].append(b - 1)
    graphs[b - 1].append(a - 1)


start_point = 0
inf = float('inf')
dps = [inf for _ in range(N)]
dps[0] = 0
queue = deque([[start_point, 0, 0]])
# print(taxies)
# print(graphs)
while queue:
    now_point, now_cost, remain_point = queue.popleft()
    # print(now_point, now_cost, remain_point)

    for next_point in graphs[now_point]:
        # remain_pointがまだある場合には突き進むのができる
        if remain_point >= 1:
            queue.append([next_point, now_cost, remain_point - 1])
        # 乗り換える場合にはチェックが必要。
        cost, next_remain_point = taxies[now_point]
        if dps[now_point] >= now_cost:
            dps[now_point] = now_cost
            queue.append([next_point, now_cost + cost, next_remain_point - 1])


print(dps[N - 1])
