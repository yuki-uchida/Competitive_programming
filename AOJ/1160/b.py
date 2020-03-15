import sys

sys.setrecursionlimit(20000)


def dfs(seen_points, squares, i, j, w, h):
    seen_points.append([i, j])
    if i >= 1 and j >= 1:
        if [i - 1, j - 1] not in seen_points and squares[i - 1][j - 1] == 1:
            dfs(seen_points, squares, i - 1, j - 1, w, h)
    if i >= 1:
        if [i - 1, j] not in seen_points and squares[i - 1][j] == 1:
            dfs(seen_points, squares, i - 1, j, w, h)
    if j >= 1:
        if [i, j - 1] not in seen_points and squares[i][j - 1] == 1:
            dfs(seen_points, squares, i, j - 1, w, h)
    if j >= 1 and i + 1 <= h:
        if [i + 1, j - 1] not in seen_points and squares[i + 1][j - 1] == 1:
            dfs(seen_points, squares, i + 1, j - 1, w, h)
    if i + 1 <= h:
        if [i + 1, j] not in seen_points and squares[i + 1][j] == 1:
            dfs(seen_points, squares, i + 1, j, w, h)
    if j + 1 <= w and i + 1 <= h:
        if [i + 1, j + 1] not in seen_points and squares[i + 1][j + 1] == 1:
            dfs(seen_points, squares, i + 1, j + 1, w, h)
    if j + 1 <= w:
        if [i, j + 1] not in seen_points and squares[i][j + 1] == 1:
            dfs(seen_points, squares, i, j + 1, w, h)
    if i >= 1 and j + 1 <= w:
        if [i - 1, j + 1] not in seen_points and squares[i - 1][j + 1] == 1:
            dfs(seen_points, squares, i - 1, j + 1, w, h)


counts = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    squares = []
    for _ in range(h):
        squares.append(list(map(int, input().split())))
    seen_points = []
    count = 0
    for i, square in enumerate(squares):
        for j, point in enumerate(square):
            if point == 1 and [i, j] not in seen_points:
                dfs(seen_points, squares, i, j, w - 1, h - 1)
                count += 1
    counts.append(count)

for count in counts:
    print(count)
