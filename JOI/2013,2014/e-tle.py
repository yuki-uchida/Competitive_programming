from collections import deque
N, K = map(int, input().split())
taxi_companies = []
for _ in range(N):
    taxi_companies.append(list(map(int, input().split())))
loads = [[] for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    loads[a - 1].append(b - 1)
    loads[b - 1].append(a - 1)
inf = float('inf')

# print(taxi_companies)
# print(loads)


def bfs(start):
    dps = [inf] * N
    dps[start] = 0
    queue = deque([[start, 0]])
    _, remain_point = taxi_companies[start]
    ret = set([])
    while queue:
        now_point, now_cost = queue.popleft()
        if dps[now_point] < now_cost:
            continue
        for next_point in loads[now_point]:
            if dps[next_point] > now_cost + 1:
                dps[next_point] = now_cost + 1
                queue.append([next_point, now_cost + 1])
            if now_cost + 1 <= remain_point and next_point != start:
                ret.add(next_point)
    #     print(dps)
    # print('===============')
    return ret


can_go_cities = [[] for _ in range(N)]
for i in range(N):
    can_go_cities[i] = bfs(i)
# print(can_go_cities)


def dikstra(start, goal):
    dps = [inf for _ in range(N)]
    queue = deque([[start, 0]])
    dps[start] = 0
    while queue:
        now_point, now_cost = queue.popleft()
        if dps[now_point] < now_cost:
            continue
        for next_point in can_go_cities[now_point]:
            cost, _ = taxi_companies[now_point]
            if dps[next_point] > now_cost + cost:
                dps[next_point] = now_cost + cost
                queue.append([next_point, now_cost + cost])
        # print(now_point, now_cost, dps)
    return dps[goal]


# どういう時に打ち切る？
# 進めるだけ進んで、そこにたどり着いた時のコストがdps[now]よりも大きい時
# dpsの更新はタクシーを乗り換えた時のみ


min_cost = dikstra(0, N - 1)
print(min_cost)
