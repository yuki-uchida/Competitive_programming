n = int(input())

graphs = []

for _ in range(n):
    graphs.append(list(map(int, input().split()))[2:])


def bfs(graphs, seen_points, score, scores, queue):
    while len(queue) > 0:
        start_point = queue.pop(0)
        if seen_points[start_point - 1] == 2:
            continue
        else:
            next_points = [
                point for point in graphs[start_point - 1] if seen_points[point - 1] == 0]
            if len(next_points) >= 1:
                score += 1
                for point in next_points:
                    queue.append(point)
                    if seen_points[point - 1] == 0:
                        seen_points[point - 1] = 1
                        scores[point - 1] = scores[start_point - 1] + 1
                seen_points[start_point - 1] = 2


seen_points = [0 for _ in range(n)]
scores = [-1 for _ in range(n)]
scores[0] = 0
queue = [1]
bfs(graphs, seen_points, 0, scores, queue)

for index, score in enumerate(scores):
    print(index + 1, score)
