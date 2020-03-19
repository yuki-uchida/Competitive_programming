R, C = map(int, input().split())
start_row, start_col = map(int, input().split())
goal_row, goal_col = map(int, input().split())

squares = []
for _ in range(R):
    squares.append(list(input()))
scores = [[R * C for _ in range(C)] for _ in range(R)]

# print(squares)


def bfs(squares, scores, start_row, start_col):
    seen_points = []
    mv = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = [[start_row, start_col]]
    scores[start_row - 1][start_col - 1] = 0
    while len(queue) > 0:
        start_row, start_col = queue.pop(0)
        if [start_row, start_col] not in seen_points:
            seen_points.append([start_row, start_col])
            # print(start_row,
            #       start_col)
            for next_postion in mv:
                if start_row + next_postion[0] > 0 and start_row + next_postion[0] <= R and start_col + next_postion[1] > 0 and start_col + next_postion[1] <= C:
                    if squares[start_row + next_postion[0] - 1][start_col + next_postion[1] - 1] == '.':
                        if scores[start_row + next_postion[0] - 1][start_col + next_postion[1] - 1] > (scores[start_row - 1][start_col - 1] + 1):
                            queue.append(
                                [start_row + next_postion[0], start_col + next_postion[1]])
                            scores[start_row + next_postion[0] - 1
                                   ][start_col + next_postion[1] - 1] = scores[start_row - 1][start_col - 1] + 1


bfs(squares, scores, start_row, start_col)
# print(scores)
print(scores[goal_row - 1][goal_col - 1])
