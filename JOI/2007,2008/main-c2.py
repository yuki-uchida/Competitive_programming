# N <= 1000
# M <= 2*10**8

N, M = map(int, input().split())

points = [int(input()) for _ in range(N)]
points.append(0)
# M を超えない程度に最大値を取りたい.
# ダーツを投げる数はN本まで。0本でもいい


# 二本組み合わせた時の数値を出してソートする
# その数の組み合わせをだす。


# double_scores = set()
# for i in range(N + 1):
#     for j in range(i, N + 1):
#         if points[i] + points[j] <= M:
#             double_scores.add(points[i] + points[j])


double_scores = [0] * ((N + 2) * (N + 1) // 2)
count = 0

for i in range(N + 1):
    for j in range(i, N + 1):
        # print(count, i, j)
        double_scores[count] = points[i] + points[j]
        count += 1

double_scores.sort()
# print(double_scores)


def left_binary_search(target):
    left = 0
    right = len(double_scores) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if target < double_scores[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


double_scores = sorted(double_scores)
# print(double_scores)
ans = 0
for score in double_scores:
    target = M - score
    if target < 0:
        continue
    # print(left_binary_search(target, double_scores))
    ans = max(
        ans, score + double_scores[left_binary_search(target)])
print(ans)
