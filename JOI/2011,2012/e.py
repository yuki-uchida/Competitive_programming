from collections import deque
import sys
input = sys.stdin.readline
W, H = list(map(int, input().split()))
must_points = []
buildings = []
for i in range(H):
    input_text = list(map(int, input().split()))
    for j, text in enumerate(input_text):
        if text == 1:
            must_points.append([i, j])
    buildings.append(input_text)

print(*buildings)
print(must_points)
# 2:10 3:12 4:14 5:16
# yが奇数の時は、[0,-1][1,1][-1,0][1,0][0,1][1,1]
# yが偶数の時は、[-1,-1][0,-1][-1,0][1,0][-1,1][0,1]


def bfs(buildings, start_point):
    # 遅かったらここに注目
    concat_points = [start_point]
    queue = deque([])
    queue.append(start_point)
    while queue:
        now_point = queue.popleft()
        if (now_point[0] + 1) % 2 == 0:
            mv = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0]]
        else:
            mv = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0], [1, 1]]
        for next_position in mv:
            next_point = [now_point[0] + next_position[0],
                          now_point[1] + next_position[1]]
            if not(0 <= next_point[0] < H) or not(0 <= next_point[1] < W):
                continue
            if buildings[next_point[0]][next_point[1]] == 0:
                continue
            if next_point in concat_points:
                continue
            concat_points.append(next_point)
            queue.append(next_point)
    return concat_points


all_concat_points = []
seen_points = []
for must_point in must_points:
    if must_point in seen_points:
        continue
    concat_points = bfs(buildings, must_point)
    all_concat_points.append(concat_points)
    for point in concat_points:
        seen_points.append(point)
print(all_concat_points)


# 計算方法がわからん！
total_costs = []
for concat_points in all_concat_points:
    cost = []
    while_points = []
    for point in concat_points:
        plus_point = 0
        if (point[0] + 1) % 2 == 0:
            mv = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0]]
        else:
            mv = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0], [1, 1]]
        for check_position in mv:
            check_point = [point[0] + check_position[0],
                           point[1] + check_position[1]]
            if check_point not in concat_points:
                plus_point += 1
        cost.append(plus_point)
    print(cost)
    total_costs.append(sum(cost))

print(total_costs)
print(sum(total_costs))
