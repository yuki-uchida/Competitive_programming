# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d
# DP
import sys
input = sys.stdin.readline
# int(input()) # 入力が1つ
d, n = map(int, input().split())  # 入力が複数
temperature = []
for _ in range(d):
    t = int(input())
    temperature.append(t)

clothes = []
for _ in range(n):
    a, b, c = map(int, input().split())
    clothes.append((a, b, c))

inf = float('inf')
dp = [[-inf] * n for _ in range(d)]
for i in range(d):
    t = temperature[i]
    for j in range(n):
        a, b, c = clothes[j]
        if a <= t <= b:
            if i == 0:
                dp[i][j] = 0
            else:
                for k in range(n):
                    _, _, pre = clothes[k]
                    dp[i][j] = max(dp[i][j], abs(c - pre) + dp[i - 1][k])
ans = max(dp[-1])
# print(dp)
print(ans)
