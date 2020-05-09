from collections import deque
N, M, K, S = map(int, input().split())
# N個の町があり、K個の町がゾンビに支配されている
# M本の道路がある
# ゾンビに支配されている町から、S本以下の道路を使って到達されてしまう町は危険な町
P, Q = map(int, input().split())
# 危険でない町ではP円
# 危険な町ではQ円かかる
danger_towns = [0 for _ in range(N)]
for i in range(K):
    danger_towns[int(input()) - 1] = 2
loads = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    loads[A - 1].append(B - 1)
    loads[B - 1].append(A - 1)
# print(loads)
# print(danger_towns)
# まずは危険な町を洗い出す必要がある。
for town_index, town_situation in enumerate(danger_towns):
    if town_situation != 2:
        continue
    queue = deque([[town_index, 0]])
    while queue:
        now_town, now_cost = queue.popleft()
        for next_town in loads[now_town]:
            if S >= now_cost + 1:
                if danger_towns[next_town] == 2:
                    continue
                danger_towns[next_town] = 1
                queue.append([next_town, now_cost + 1])


# print(danger_towns)
inf = float('inf')

# print(P, Q)


def dikstra(start, goal, loads):
    dps = [inf for _ in range(N)]
    dps[start] = 0
    queue = deque([[start, 0]])
    while queue:
        now_point, now_cost = queue.popleft()
        if dps[now_point] < now_cost:
            continue
        for next_point in loads[now_point]:
            if danger_towns[next_point] == 2:
                continue
            elif danger_towns[next_point] == 1:
                if dps[next_point] > now_cost + Q:
                    dps[next_point] = now_cost + Q
                    queue.append([next_point, dps[next_point]])
            elif danger_towns[next_point] == 0:
                if dps[next_point] > now_cost + P:
                    dps[next_point] = now_cost + P
                    queue.append([next_point, dps[next_point]])
        # print(now_point, dps)
    if danger_towns[goal] == 0:
        return dps[goal] - P
    else:
        return dps[goal] - Q


min_cost = dikstra(0, N - 1, loads)
print(min_cost)
