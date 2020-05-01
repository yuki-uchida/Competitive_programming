import itertools

N, M = map(int, input().split())
dolls = {}
first_dolls = []
for _ in range(N):
    num = int(input())
    first_dolls.append(num)
    if num in dolls:
        dolls[num] += 1
    else:
        dolls[num] = 1
# print(dolls)
# print(first_dolls)
nums_permutations = list(
    map(list, itertools.permutations(dolls.keys(), len(dolls.keys()))))

arrangements = []
for nums_permutation in nums_permutations:
    arrangement = []
    for num in nums_permutation:
        arrangement.extend([num] * dolls[num])
    arrangements.append(arrangement)
inf = float('inf')
min_count = inf
for arrangement in arrangements:
    count = 0
    for num_a, num_b in itertools.zip_longest(first_dolls, arrangement):
        if num_a != num_b:
            count += 1
    min_count = min(min_count, count)
print(min_count)
