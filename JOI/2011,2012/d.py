n, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(k)]
s.sort()
# print(s)
dp = [[0, 0, 0] for i in range(n + 1)]
# n日目までで最新のメニューがトマト＝dp[n][1]
x = 0

for i in range(n):
    if i + 1 == 1:
        if i + 1 != s[x][0]:
            dp[1][0] = 1
            dp[1][1] = 1
            dp[1][2] = 1
        else:
            dp[1][s[x][1] - 1] = 1
            if x < k - 1:
                x += 1
        continue

    # メニューが決定済みでない時
    if i + 1 != s[x][0]:
        for j in range(3):
            if dp[i][j] != 0:
                dp[i + 1][j] += sum(dp[i]) - dp[i - 1][j]
            else:
                dp[i + 1][j] += sum(dp[i])
        # 死んだ遷移を消す
        for j in range(3):
            if dp[i][j] != 0:
                dp[i][j] -= dp[i - 1][j]

    else:
        if dp[i][s[x][1] - 1] != 0:
            dp[i + 1][s[x][1] - 1] += sum(dp[i]) - dp[i - 1][s[x][1] - 1]
            dp[i][s[x][1] - 1] -= dp[i - 1][s[x][1] - 1]

        else:
            dp[i + 1][s[x][1] - 1] += sum(dp[i])
        if x < k - 1:
            x += 1
# print(dp)
print(sum(dp[n]) % 10000)
