from collections import deque
n, k = map(int, input().split())
graphs = [[] for _ in range(n)]
inf = float('inf')
for _ in range(k):
    inputs_text = list(map(int, input().split()))
    if len(inputs_text) == 4:
        c, d, e = inputs_text[1:]
        graphs[c - 1].append([d - 1, e])
        graphs[d - 1].append([c - 1, e])
    else:
        a, b = inputs_text[1:]
        start_point = a - 1
        goal_point = b - 1
        queue = deque([[start_point, 0]])
        dps = [inf for _ in range(n)]
        dps[start_point] = 0
        while queue:
            now_point, prev_cost = queue.popleft()
            if dps[now_point] < prev_cost:
                continue
            for next_point, cost in graphs[now_point]:
                if dps[next_point] < prev_cost + cost:
                    continue
                dps[next_point] = prev_cost + cost
                queue.append([next_point, dps[next_point]])
        if dps[goal_point] == inf:
            print(-1)
        else:
            print(dps[goal_point])
