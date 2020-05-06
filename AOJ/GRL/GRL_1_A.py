
from collections import deque
V, E, r = map(int, input().split())
inf = float('inf')
graphs = [[] for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    graphs[s].append([t, d])
# print(graphs)
start_point = r

dps = [inf for _ in range(V)]
dps[r] = 0
queue = deque([[r, 0]])
while queue:
    now_point_index, now_distance = queue.popleft()
    if dps[now_point_index] < now_distance:
        continue
    for next_point_index, next_distance in graphs[now_point_index]:
        if dps[next_point_index] > now_distance + next_distance:
            dps[next_point_index] = now_distance + next_distance
            queue.append([next_point_index, dps[next_point_index]])

# print(dps)
for num in dps:
    if num == inf:
        print("INF")
    else:
        print(num)
