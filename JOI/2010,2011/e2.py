from collections import deque
import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
start_position = []
cheese_positions = [[] for _ in range(N)]
areas = []
for i in range(H):
    texts = list(input().rstrip())
    for j, char in enumerate(texts):
        if char == 'S':
            start_position = [i, j]
        elif char == 'X':
            pass
        elif char == '.':
            pass
        else:
            # print(char)
            cheese_positions[int(char) - 1] = [i, j]
    areas.append(texts)

# Sはスタート(巣)　Xは障害物　1-9はチーズ

# 順番に硬さが1-Nのチーズに向かっていけば良い
move_positions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
inf = float('inf')


def bfs(start_position, goal_position):
    scores = [[inf for _ in range(W)] for _ in range(H)]
    queue = deque([start_position])
    count = 0
    scores[start_position[0]][start_position[1]] = 0
    while queue:
        now_position = queue.popleft()
        for move_position in move_positions:
            next_position = [now_position[0] + move_position[0],
                             now_position[1] + move_position[1]]
            if 0 <= next_position[0] <= H - 1 and 0 <= next_position[1] <= W - 1:
                if areas[next_position[0]][next_position[1]] == 'X':
                    continue
                if scores[next_position[0]][next_position[1]] > scores[now_position[0]][now_position[1]] + 1:
                    scores[next_position[0]][next_position[1]
                                             ] = scores[now_position[0]][now_position[1]] + 1
                    queue.append(next_position)
    # print(scores)
    return scores[goal_position[0]][goal_position[1]]


costs = 0
cheese_positions.insert(0, start_position)
# print(cheese_positions)
for i in range(1, len(cheese_positions)):
    cost = bfs(cheese_positions[i - 1], cheese_positions[i])
    costs += cost
print(costs)
