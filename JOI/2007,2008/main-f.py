from collections import deque
n, k = map(int, input().split())

islands = [[] for _ in range(n)]
inf = float('inf')


def dikstra(start, goal, islands):
    # print(islands)
    dps = [inf for _ in range(len(islands))]
    queue = deque([[start, 0]])
    while queue:
        # print(queue)
        now_point, now_cost = queue.popleft()
        if dps[now_point] < now_cost:
            continue
        for next_point, next_cost in islands[now_point]:
            if dps[next_point] > now_cost + next_cost:
                dps[next_point] = now_cost + next_cost
                queue.append([next_point, now_cost + next_cost])
    # print(dps)
    return dps[goal]


for i in range(k):
    input_text = list(map(int, input().split()))
    if input_text[0] == 0:
        start_island, goal_island = input_text[1:]
        cost = dikstra(start_island - 1, goal_island - 1, islands)
        if cost == inf:
            print('-1')
        else:
            print(cost)
    else:
        load_a, load_b, cost = input_text[1:]
        islands[load_a - 1].append([load_b - 1, cost])
        islands[load_b - 1].append([load_a - 1, cost])

# 3 8
# 1 3 1 10
# 0 2 3
# 1 2 3 20
# 1 1 2 5
# 0 3 2
# 1 1 3 7
# 1 2 1 9
# 0 2 3
