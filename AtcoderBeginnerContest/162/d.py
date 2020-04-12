import bisect
N = int(input())  # N<= 4000 6*10^10なので、削減しないとだめ
S = list(input())


# Si Sj Skがどれも別のもの。ただしi<j<k
# また、j-i != k-j
# 1,2,3はだめ1,2,4はok
# 1,3,5もだめ
# この組の数を求める

# count = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             if j - i != k - j:
#                 if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
#                     count += 1


indexes = {'R': [], "G": [], "B": []}
for i, char in enumerate(S):
    indexes[char].append(i + 1)
# print(permutation_hash)
count = 0
R_indexes_count = len(indexes['R'])
G_indexes_count = len(indexes['G'])
B_indexes_count = len(indexes['B'])
indexes_count = {'R': R_indexes_count,
                 'G': G_indexes_count, 'B': B_indexes_count}
# 短いやつを使うとかする？,
if R_indexes_count <= G_indexes_count and R_indexes_count <= B_indexes_count:
    min_type = 'R'
    if G_indexes_count <= B_indexes_count:
        second_min_type = 'G'
        last_type = 'B'
    else:
        second_min_type = 'B'
        last_type = 'G'
elif G_indexes_count <= R_indexes_count and G_indexes_count <= B_indexes_count:
    min_type = 'G'
    if R_indexes_count <= B_indexes_count:
        second_min_type = 'R'
        last_type = 'B'
    else:
        second_min_type = 'B'
        last_type = 'R'
else:
    min_type = 'B'
    if G_indexes_count <= R_indexes_count:
        second_min_type = 'G'
        last_type = 'R'
    else:
        second_min_type = 'R'
        last_type = 'G'

# print(min_type, second_min_type, last_type)
for R_index in indexes[min_type]:
    for G_index in indexes[second_min_type]:
        middle_index = (R_index + G_index) / 2
        remove_conut = 0
        if middle_index != R_index and middle_index != G_index:
            if middle_index in indexes[last_type]:
                remove_conut += 1
        div = abs(G_index - R_index)
        if G_index < R_index:
            if G_index - div in indexes[last_type]:
                remove_conut += 1
            if R_index + div in indexes[last_type]:
                remove_conut += 1
        else:
            if G_index + div in indexes[last_type]:
                remove_conut += 1
            if R_index - div in indexes[last_type]:
                remove_conut += 1
        count += (indexes_count[last_type] - remove_conut)

print(count)
