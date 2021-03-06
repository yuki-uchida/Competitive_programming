N, M = map(int, input().split())

counts_each_doll = [[0 for _ in range(N + 1)] for _ in range(M)]
dolls_count = [0 for _ in range(M)]

for i in range(1, N + 1):
    doll_index = int(input()) - 1
    dolls_count[doll_index] += 1
    for j in range(M):
        if doll_index == j:
            counts_each_doll[j][i] += counts_each_doll[j][i - 1] + 1
        else:
            counts_each_doll[j][i] += counts_each_doll[j][i - 1]
# print(dolls_count)

dolls_permutations_count = [0 for _ in range(1 << M)]
for bit in range(1 << M):
    for j in range(M):
        if bit & (1 << j):
            dolls_permutations_count[bit] += dolls_count[j]
# print(dolls_permutations_count)
inf = float('inf')

# ぬいぐるみの組み合わせ分用意しておく
dps = [inf for _ in range(1 << M)]
dps[0] = 0

for bit in range(1 << M):
    for i in range(M):
        if bit & (1 << i):
            continue
        next_bit = bit | (1 << i)
        need_right_dolls = dolls_permutations_count[next_bit]
        need_left_dolls = dolls_permutations_count[bit]
        need_dolls = need_right_dolls - need_left_dolls
        exists_dolls = counts_each_doll[i][need_right_dolls] - \
            counts_each_doll[i][need_left_dolls]
        cost = need_dolls - exists_dolls
        dps[next_bit] = min(dps[next_bit], dps[bit] + cost)
# print(dps)
print(dps[(1 << M) - 1])
