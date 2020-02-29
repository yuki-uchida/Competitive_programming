import itertools

n = int(input())
a = list(map(int, input().split(" ")))
q = int(input())


sums_set = set()

for i in range(1, n + 1):
    sums_set |= set(sum(combination)
                    for combination in itertools.combinations(a, i))

want_nums = list(map(int, input().split(" ")))
for want_num in want_nums:
    if want_num in sums_set:
        print("yes")
    else:
        print("no")
