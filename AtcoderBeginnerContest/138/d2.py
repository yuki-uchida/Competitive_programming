from collections import deque
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
bars = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    bars[a - 1].append(b - 1)
    bars[b - 1].append(a - 1)

# 併せられるものは足し算して合わせる
# 直線形式に変更する
points = [0 for _ in range(N)]
for _ in range(Q):
    i, point = map(int, input().split())
    points[i - 1] += point
# print(bars)
# print(points)
# counters = [0 for _ in range(N)]
# 一つの処理ごとに全てのルートをわりだすとMAXでQN回処理する事になる
# でも、DPっぽく根の上から足して、次の処理をやると削減できる。
#　なので、points[next_index] += points[now_index] とやると、足していける
seen_points = [False for _ in range(N)]
queue = deque([0])
while queue:
    now_index = queue.pop()
    seen_points[now_index] = True
    for next_index in bars[now_index]:
        if not seen_points[next_index]:
            points[next_index] += points[now_index]
            queue.append(next_index)
# print(points)
print(*points)
