M, N = map(int, input().split())
K = int(input())
areas = [[[0 for _ in range(N + 1)] for _ in range(M + 1)] for _ in range(3)]
for i in range(1, M + 1):
    input_text = list(input())
    for j in range(1, N + 1):
        if input_text[j - 1] == 'J':
            areas[0][i][j] = areas[0][i][j - 1] + areas[0][i - 1][j] - areas[0][i - 1][j - 1] + 1
            areas[1][i][j] = areas[1][i][j - 1] + areas[1][i - 1][j] - areas[1][i - 1][j - 1]
            areas[2][i][j] = areas[2][i][j - 1] + areas[2][i - 1][j] - areas[2][i - 1][j - 1]
        elif input_text[j - 1] == 'O':
            areas[0][i][j] = areas[0][i][j - 1] + areas[0][i - 1][j] - areas[0][i - 1][j - 1]
            areas[1][i][j] = areas[1][i][j - 1] + areas[1][i - 1][j] - areas[1][i - 1][j - 1] + 1
            areas[2][i][j] = areas[2][i][j - 1] + areas[2][i - 1][j] - areas[2][i - 1][j - 1]
        else:
            areas[0][i][j] = areas[0][i][j - 1] + areas[0][i - 1][j] - areas[0][i - 1][j - 1]
            areas[1][i][j] = areas[1][i][j - 1] + areas[1][i - 1][j] - areas[1][i - 1][j - 1]
            areas[2][i][j] = areas[2][i][j - 1] + areas[2][i - 1][j] - areas[2][i - 1][j - 1] + 1
# print(areas)

for _ in range(K):
    h1, w1, h2, w2 = map(int, input().split())
    j_count = areas[0][h2][w2] - (areas[0][h2][w1 - 1] + areas[0][h1 - 1][w2] - areas[0][h1 - 1][w1 - 1])
    o_count = areas[1][h2][w2] - (areas[1][h2][w1 - 1] + areas[1][h1 - 1][w2] - areas[1][h1 - 1][w1 - 1])
    i_count = areas[2][h2][w2] - (areas[2][h2][w1 - 1] + areas[2][h1 - 1][w2] - areas[2][h1 - 1][w1 - 1])
    print(j_count, o_count, i_count)
