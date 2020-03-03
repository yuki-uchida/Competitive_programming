# 1<=N<=12
# 0<=M<=NC2
import itertools
N, M = list(map(int, input().split()))
friendships = []
for _ in range(M):
    a, b = tuple(map(int, input().split()))
    friendships.append((a - 1, b - 1))

members = []
for i in range(2**N):
    member = []
    for j in range(N):
        if((i >> j) & 1):
            member.append(1)
        else:
            member.append(0)
    indexes = []
    for i, human in enumerate(member):
        if human:
            indexes.append(i)
    members.append(indexes)

max_count = 0
for member in members:
    all_combinations = [
        combination for combination in itertools.combinations(member, 2)]
    check = True
    for combination in all_combinations:
        if combination in friendships:
            continue
        else:
            check = False
    if check and max_count < len(member):
        max_count = len(member)
print(max_count)
