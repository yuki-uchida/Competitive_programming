from collections import deque
import heapq
N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
graphs = [[] for _ in range(N)]
dangers = [1 for _ in range(N)]
dangers_index = []
for _ in range(K):
    c = int(input())
    dangers[c - 1] = -1
    dangers_index.append(c - 1)
    # dangerな町からS本以下でたどり着ける街は危険な街(0)
for i in range(M):
    A, B = map(int, input().split())
    graphs[A - 1].append(B - 1)
    graphs[B - 1].append(A - 1)
    # print(i)
# print('aaaaaaaaaaaaaaaaaaaa')
inf = float('inf')
dps = [[inf for _ in range(len(dangers_index))] for _ in range(len(dangers_index))]
# print(dangers)


dis = [inf for _ in range(N)]
for i in dangers_index:
    if dangers[i] == -1:
        queue = deque([[i, 0]])
        while queue:
            now_point, now_cost = queue.popleft()
            if now_cost >= S or now_cost >= dis[now_point]:
                continue
            dis[now_point] = now_cost
            for next_point in graphs[now_point]:
                if dangers[next_point] == -1:
                    continue
                dangers[next_point] = 0
                if now_cost + 1 >= S:
                    continue
                queue.append([next_point, now_cost + 1])
        # print(dis)
# print(dangers)
# print(graphs)
start_point = 0
goal_point = N - 1
queue = []
heapq.heappush(queue, (0, start_point))

dps = [inf for _ in range(N)]
while queue:
    now_cost, now_point = heapq.heappop(queue)
    if dps[now_point] < now_cost:
        continue
    for next_point in graphs[now_point]:
        if dangers[next_point] == -1:
            continue
        elif dangers[next_point] == 0:
            cost = Q
        else:
            cost = P
        if dps[next_point] <= now_cost + cost:
            continue
        dps[next_point] = now_cost + cost
        heapq.heappush(queue, (dps[next_point], next_point))

if dangers[goal_point] == 0:
    print(dps[goal_point] - Q)
else:
    print(dps[goal_point] - P)
