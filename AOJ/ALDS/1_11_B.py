n = int(input())

points = []
seen = []
find_time = []
end_time = []
for _ in range(n):
    input_text = list(map(int, input().split()))
    u, k, v_list = input_text[0], input_text[1], input_text[2:]
    seen.append(False)
    points.append(v_list)
    find_time.append(0)
    end_time.append(0)

count = [0]


def dfs(graph, v, count):
    seen[v] = True
    find_time[v] = count[0]
    for next_v in graph[v]:
        if seen[next_v - 1]:
            continue
        count[0] += 1
        dfs(graph, next_v - 1, count)
    count[0] += 1
    end_time[v] = count[0]


for index, seen_point in enumerate(seen):
    if seen_point:
        pass
    else:
        count[0] += 1
        dfs(points, index, count)
# print(find_time)
# print(end_time)


count = 1
for f, e in zip(find_time, end_time):
    print(count, f, e)
    count += 1
