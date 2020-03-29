from collections import deque
N, X, Y = map(int, input().split())
graphs = [[i - 1, i + 1] for i in range(1, N - 1)]
graphs.insert(0, [1])
graphs.append([N - 2])

# scores = [0 for _ in range(N)]

graphs[X - 1].append(Y - 1)
# print(graphs)


# 数をカウントする
counts = [0 for _ in range(N)]


for index, start_point in enumerate(graphs):
    scores = [10**9 + 7 for _ in range(N)]
    queue = deque([index])
    scores[index] = 0
    while queue:
        now_index = queue.pop()
        for next_index in graphs[now_index]:
            if scores[next_index] > scores[now_index] + 1:
                queue.append(next_index)
                scores[next_index] = scores[now_index] + 1
    for score in scores[index:]:
        counts[score] += 1

for count in counts[1:]:
    print(count)
