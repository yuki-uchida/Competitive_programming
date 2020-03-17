import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
exist_floors = []

all_floors = []
for _ in range(n):
    all_floors.append(list(map(int, input().split())))

# print(all_floors)
seen_points = []


def dfs(all_floors, start_i, start_j, score, scores, seen_points):
    seen_points.append([start_i, start_j])
    mvs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for mv in mvs:
        next_i, next_j = start_i + mv[0], start_j + mv[1]
        if [next_i, next_j] not in seen_points:
            if 0 <= next_i and next_i <= n - 1 and 0 <= next_j and next_j <= m - 1:
                if all_floors[next_i][next_j] == 1:
                    dfs(all_floors, next_i, next_j,
                        score + 1, scores, seen_points)
    seen_points.pop(-1)
    # print(score)
    scores.append(score)


all_pattern_scores = []
for i in range(n):
    # print('---------')
    for j in range(m):
        # print('===========')
        seen_points = []
        scores = []
        if all_floors[i][j] == 1:
            dfs(all_floors, i, j, 1, scores, seen_points)
            all_pattern_scores.append(max(scores))


# print(all_pattern_scores)[]

print(max(all_pattern_scores))
