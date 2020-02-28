M = int(input())
want_stars = []
for _ in range(M):
    want_stars.append(list(map(int, input().split(" "))))
N = int(input())
exist_stars = []
for _ in range(N):
    exist_stars.append(list(map(int, input().split(" "))))

move_x = 0
move_y = 0
ans_x = 0
ans_y = 0
for exist_star in exist_stars:
    move_x, move_y = exist_star[0] - \
        want_stars[0][0], exist_star[1] - want_stars[0][1]
    exist_count = 0
    for want_star in want_stars:
        if [want_star[0] + move_x, want_star[1] + move_y] in exist_stars:
            exist_count += 1
        else:
            break
    if exist_count == M:
        ans_x, ans_y = move_x, move_y
        break
print(str(ans_x) + " " + str(ans_y))
