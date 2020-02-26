N = int(input())

points = []
max_point = 101
min_point = -1
for _ in range(N):
    a, b = map(int, input().split(" "))
    max_point = min([a, b, max_point])
    min_point = max([a, b, min_point])
    points.append([a, b])

# print(points)
# print(max_point, min_point)

all_seconds = []
# pointsの中に入っているもの以外を入口と出口に設定する必要はない
for i in range(N):
    for j in range(N):
        total_second = 0
        for a, b in points:
            second = abs(a - points[i][0]) + \
                (b - a) + abs(b - points[j][1])
            total_second += second
        all_seconds.append(total_second)
print(min(all_seconds))
