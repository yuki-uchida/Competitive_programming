
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import deque

# n行m列
m, n = map(int, input().split())
a = []
# 上下に一行挿入する
for i in range(n + 2):
    if i == 0 or i == n + 1:
        a.append([0] * (m + 2))
    else:
        b = list(map(int, input().split()))
        a.append([0] + b + [0])

# print(a)
d = deque([[0, 0]])


def move(x, y):
    a[x][y] = -1
    # 偶数行の処理
    if x % 2 == 0:
        dxy = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0]]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx > n + 1 or ny < 0 or ny > m + 1:
                continue
            if a[nx][ny] == 0:
                a[nx][ny] = -1
                d.append([nx, ny])
    # 奇数行の処理
    else:
        dxy = [[-1, 1], [-1, 0], [0, -1], [0, 1], [1, 1], [1, 0]]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx > n + 1 or ny < 0 or ny > m + 1:
                continue
            if a[nx][ny] == 0:
                a[nx][ny] = -1
                d.append([nx, ny])


while d:
    ij = d.popleft()
    i, j = ij
    move(i, j)


def check(x, y):
    res = 0
    if x % 2 == 0:
        dxy = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0]]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if a[nx][ny] == -1:
                res += 1
        return res
    else:
        dxy = [[-1, 1], [-1, 0], [0, -1], [0, 1], [1, 1], [1, 0]]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if a[nx][ny] == -1:
                res += 1
        return res


res = 0
for i in range(n + 2):
    for j in range(m + 2):
        if a[i][j] == 1:
            num = check(i, j)
            # print(i, j, num)
            res += num
print(res)
