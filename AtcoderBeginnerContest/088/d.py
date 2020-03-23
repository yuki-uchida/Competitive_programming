import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import deque
H, W = map(int, input().split())
areas = []

black_count = 0
for _ in range(H):
    text = list(input().rstrip())
    for char in text:
        if char == '#':
            black_count += 1
    areas.append(text)

# 最短経路探索でかかったコストを使えば、コストが計算できる。全てのますの数から、最初から黒に塗られているを引いて、さらに最短コストを引けば良い
# 0,0からH,wへ行く


def bfs(areas, start_point, goal_point):
    scores = [[10**9 + 7 for _ in range(W)] for _ in range(H)]
    scores[0][0] = 1
    mv = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = deque([start_point])
    while queue:
        now_point = queue.popleft()
        for next_postion in mv:
            next_point = [now_point[0] + next_postion[0],
                          now_point[1] + next_postion[1]]
            if 0 <= next_point[0] < H and 0 <= next_point[1] < W:
                if areas[next_point[0]][next_point[1]] == '#':
                    continue
                if scores[next_point[0]][next_point[1]] > scores[now_point[0]][now_point[1]] + 1:
                    queue.append(next_point)
                    scores[next_point[0]][next_point[1]
                                          ] = scores[now_point[0]][now_point[1]] + 1
    if scores[goal_point[0]][goal_point[1]] == 10**9 + 7:
        return -1
    return scores[goal_point[0]][goal_point[1]]


cost = bfs(areas, [0, 0], [H - 1, W - 1])
if cost == -1:
    print(cost)
else:
    print(H * W - black_count - cost)
