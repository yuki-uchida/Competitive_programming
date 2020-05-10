# 1<= N,M <=12
# 1<= X <=10**5
# 1<= C <= 10**5
# 0<= A <=10**5
from itertools import combinations
N, M, X = map(int, input().split())

books = [list(map(int, input().split())) for _ in range(N)]
min_cost = 10**100
flag = False
# print(books)
for i in range(1, M + 1):
    combies = list(map(list, (combinations(list(range(N)), i))))
    # print(combies)
    for combi in combies:
        cost = 0
        skills = [0 for _ in range(M)]
        for book_i in combi:
            cost += books[book_i][0]
            for skill_i, skill_point in enumerate(books[book_i][1:]):
                skills[skill_i] += skill_point
        # print(cost, skills)
        ok = True
        for skill_point in skills:
            if skill_point < X:
                ok = False
                break
        if ok:
            flag = True
            min_cost = min(min_cost, cost)
if flag:
    print(min_cost)
else:
    print(-1)
