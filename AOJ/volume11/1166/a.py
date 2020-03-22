import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import deque


def bfs(scores, right_bars, bottom_bars, start_point, goal_point):
    queue = deque([start_point])
    while queue:
        now_point = queue.popleft()
        mv = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        if now_point[0] == 0:
            # 上はなし
            mv.remove([-1, 0])
        if now_point[0] >= h - 1:
            # 下はなし
            mv.remove([1, 0])
        if now_point[1] == 0:
            # 左はなし
            mv.remove([0, -1])
        if now_point[1] >= w - 1:
            # 右はなし
            mv.remove([0, 1])
        for next_position in mv:
            next_point = [now_point[0] + next_position[0],
                          now_point[1] + next_position[1]]
            if next_position == [-1, 0]:  # 上　
                if bottom_bars[next_point[0]][next_point[1]] == 0 and scores[now_point[0]][now_point[1]] + 1 < scores[next_point[0]][next_point[1]]:
                    queue.append(next_point)
                    scores[next_point[0]][next_point[1]
                                          ] = scores[now_point[0]][now_point[1]] + 1
            if next_position == [0, -1]:  # 左
                if right_bars[next_point[0]][next_point[1]] == 0 and scores[now_point[0]][now_point[1]] + 1 < scores[next_point[0]][next_point[1]]:
                    queue.append(next_point)
                    scores[next_point[0]][next_point[1]
                                          ] = scores[now_point[0]][now_point[1]] + 1
            if next_position == [1, 0]:  # 下
                # print('++++++++++++++++')
                # print(scores)
                # print(right_bars)
                # print(now_point[0], now_point[1])
                # print(next_point[0], next_point[1])
                if bottom_bars[now_point[0]][now_point[1]] == 0 and scores[now_point[0]][now_point[1]] + 1 < scores[next_point[0]][next_point[1]]:
                    queue.append(next_point)
                    scores[next_point[0]][next_point[1]
                                          ] = scores[now_point[0]][now_point[1]] + 1
            if next_position == [0, 1]:  # 右
                if right_bars[now_point[0]][now_point[1]] == 0 and scores[now_point[0]][now_point[1]] + 1 < scores[next_point[0]][next_point[1]]:
                    queue.append(next_point)
                    scores[next_point[0]][next_point[1]
                                          ] = scores[now_point[0]][now_point[1]] + 1
    # print(scores)
    if scores[goal_point[0]][goal_point[1]] == (len(scores[0]) * len(scores)):
        return 0
    return scores[goal_point[0]][goal_point[1]]


costs = []
while True:
    w, h = map(int, input().split())
    if [w, h] == [0, 0]:
        break
    scores = [[w * h for _ in range(w)] for _ in range(h)]
    scores[0][0] = 1
    right_bars = []
    bottom_bars = []
    for _ in range(h - 1):
        right_bar = list(map(int, input().split()))
        bottom_bar = list(map(int, input().split()))
        right_bars.append(right_bar)
        bottom_bars.append(bottom_bar)
    right_bar = list(map(int, input().split()))
    right_bars.append(right_bar)
    start_point = [0, 0]
    goal_point = [h - 1, w - 1]
    cost = bfs(scores, right_bars, bottom_bars, start_point, goal_point)
    costs.append(cost)
for cost in costs:
    print(cost)
