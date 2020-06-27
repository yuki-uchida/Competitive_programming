import itertools
N, M = map(int, input().split())
# 1222121 のように種類が並んでくる。これを並び替えて、1112222にする必要がある
# 配置の方法は1<<M

# ぬいぐるみの種類ごとに累積和する
each_dolls_count = [[0 for _ in range(N)] for _ in range(M)]
dolls_count = [0 for _ in range(M)]
for i in range(N):
    doll = int(input())
    dolls_count[doll - 1] += 1
    each_dolls_count[doll - 1][i] += 1
for i in range(M):
    each_dolls_count[i] = list(itertools.accumulate(each_dolls_count[i]))
print(each_dolls_count)


dolls_permutations_count = [0 for _ in range(1 << M)]
for bit in range(1 << M):
    for j in range(M):
        if bit & (1 << j):
            dolls_permutations_count[bit] += dolls_count[j]
print(dolls_permutations_count)

inf = float('inf')
dps = [inf for _ in range(1 << M)]
dps[0] = 0
for S in range(1 << M):
    for j in range(M):
        if S & (1 << j):
            continue
        next_S = S | (1 << j)
        right_dolls = dolls_permutations_count[next_S]
        left_dolls = dolls_permutations_count[S]
        mid_dolls = right_dolls - left_dolls
        already_exists_dolls = each_dolls_count[j - 1][right_dolls - 1] - each_dolls_count[j - 1][left_dolls - 1]
        cost = mid_dolls - already_exists_dolls
        dps[next_S] = min(dps[next_S], dps[S] + cost)
print(dps)
print(dps[(1 << M) - 1])
