N, W = map(int, input().split())
values = []
weights = []

for _ in range(N):
    v, w = map(int, input().split())
    values.append(v)
    weights.append(w)

dps = [[0 for _ in range(W + 1)] for _ in range(N + 1)]


for i in range(N):
    for j in range(W + 1):
        if j >= weights[i]:
            check_index = j // weights[i]
            check_num = []
            check_num.append(dps[i][j])
            # check項目が多い・・・
            # for index in range(check_index + 1):
            #     check_num.append(dps[i][j - (weights[i] * index)] +
            #                      (values[i] * index))
            # dps[i][j - weights[i]] + (values[i] * (j // weights[i]))
            # check_num.append(dps[i][j - weights[i]] +
            #                  values[i])
            check_num.append(dps[i + 1][j - weights[i]] +
                             values[i])

            dps[i + 1][j] = max(check_num)
        else:
            dps[i + 1][j] = dps[i][j]

# print(dps)
print(dps[N][W])
