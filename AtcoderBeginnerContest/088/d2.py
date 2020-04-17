from collections import deque
H, W = map(int, input().split())
areas = []
blacks = 0
for _ in range(H):
    texts = list(input().rstrip())
    for char in texts:
        if char == '#':
            blacks += 1
    areas.append(texts)

# start は 0,0
# goal はH-1,W-1
# .を#に変更できる
# たくさん変更すればするほどポイントは高い
# 全部のマス - 元から#だった数 - 最短距離

inf = float('inf')


def bfs(start_point, goal_point):
    scores = [[inf for _ in range(W)] for _ in range(H)]
    queue = deque([start_point])
    scores[0][0] = 0
    move_positions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    while queue:
        now_point = queue.popleft()
        for move_position in move_positions:
            next_point = [now_point[0] + move_position[0],
                          now_point[1] + move_position[1]]
            if 0 <= next_point[0] < H and 0 <= next_point[1] < W:
                if areas[next_point[0]][next_point[1]] == '.':
                    if scores[next_point[0]][next_point[1]] > scores[now_point[0]][now_point[1]] + 1:
                        scores[next_point[0]][next_point[1]
                                              ] = scores[now_point[0]][now_point[1]] + 1
                        queue.append(next_point)
    return scores[H - 1][W - 1]


cost = bfs([0, 0], [H - 1, W - 1]) + 1
if cost == inf:
    print(-1)
else:
    print(H * W - blacks - cost)
