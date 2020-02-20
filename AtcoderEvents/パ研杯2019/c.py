N, M = list(map(int, input().split(" ")))

all_scores = []
for i in range(int(N)):
    scores = list(map(int, input().split(' ')))
    all_scores.append(scores)


group_scores = []
for i in range(M):
    for j in range(i, M):
        group_score = 0
        for k in range(N):
            max_score = max([all_scores[k][i], all_scores[k][j]])
            group_score += max_score
        group_scores.append(group_score)

print(max(group_scores))
