import sys
from collections import deque
input = sys.stdin.readline
H, W, N = map(int, input().split())

points = []
start_i = None
start_j = None
must_points = [[None, None] for _ in range(N)]
nums = [str(i + 1) for i in range(N)]
for i in range(H):
    text = list(map(str, list(input().rstrip())))
    if 'S' in text:
        start_i = i
        start_j = text.index('S')
    for j, char in enumerate(text):
        if char in nums:
            must_points[int(char) - 1] = [i, j]
    points.append(text)
# print(start_i, start_j)
# print(must_points)
start_point = [start_i, start_j]
# S: スタート 1~9: チーズの硬さ .: 何もない X:通れない
# ゴールが決まっていないのが難しそう。全てのチーズを食べなければいけない。どこで終わるかは制限がない
# 通らなければいけないところは決まっている
# 自分の体力より高い硬さは食べれない制限がある


# どうやって終わらせる？=> チーズの硬さは一意なので、もっとも大きいチーズを生み出しているところに行くまでの最短経路(ただしその一個前の数値の硬さのチーズを食べている)
# 通らなきゃいけない順番は決まっているので、bfsを各ポイントに向けてやって、全て足せば良い！
def bfs(points, start_point, goal_point):
    costs = [[W * H for _ in range(W)] for _ in range(H)]
    costs[start_point[0]][start_point[1]] = 0
    mv = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    # seen_points使わない方が早い・・・
    # 最短経路を探したいので、他の点に関しては保証しなくても良いからだと思われる・
    # seen_points = [start_point]
    queue = deque([])
    queue.append(start_point)
    while queue:
        now_point = queue.popleft()
        if now_point == goal_point:
            break
        for next_position in mv:
            next_point = [now_point[0] + next_position[0],
                          now_point[1] + next_position[1]]
            if next_point[0] < 0 or next_point[0] >= H or next_point[1] < 0 or next_point[1] >= W:
                continue
            if points[next_point[0]][next_point[1]] == 'X':
                continue
            if costs[next_point[0]][next_point[1]] <= costs[now_point[0]][now_point[1]] + 1:
                continue
            # if next_point in seen_points:
            #     continue
            # seen_points.append(next_point)
            queue.append(next_point)
            costs[next_point[0]][next_point[1]
                                 ] = costs[now_point[0]][now_point[1]] + 1
    return costs[goal_point[0]][goal_point[1]]


cost = 0
for goal_point in must_points:
    cost += bfs(points, start_point, goal_point)
    start_point = goal_point
print(cost)
