from collections import deque
V, E, R = map(int, input().split())
inf = float('inf')
graphs = [[] for _ in range(V)]

for _ in range(E):
    s, t, d = map(int, input().split())
    graphs[s].append([t, d])

start_point = R

dps = [inf for _ in range(V)]
dps[R] = 0

queue = deque([[R, 0]])
while queue:
    now_point, prev_cost = queue.popleft()
    if dps[now_point] < prev_cost:
        continue
    for next_point, cost in graphs[now_point]:
        if dps[next_point] < prev_cost + cost:
            continue
        dps[next_point] = prev_cost + cost
        queue.append([next_point, prev_cost + cost])

for ans in dps:
    if ans == inf:
        print("INF")
    else:
        print(ans)
