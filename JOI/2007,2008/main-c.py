# 合計点がMを超えてしまうと０点。超えなければS点がもらえる
import bisect
n, M = map(int, input().split())
points = [0]
for _ in range(n):
    points.append(int(input()))
# やを半分に分ける。そしてそれぞれの数字をたす。その中でM以下で最大のものを出す
n += 1
points.sort()
scores = [0] * (n * (n + 1) // 2)
print(scores)
count = 0

for i in range(n):
    for j in range(i, n):
        scores[count] = points[i] + points[j]
        count += 1

scores.sort()
max_score = 0
for temp_score in scores:
    if temp_score <= M:
        index = max(0, bisect.bisect_left(scores, (M - temp_score)) - 1)
        max_score = max(max_score, temp_score + scores[index])
print(max_score)
