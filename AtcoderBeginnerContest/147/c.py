N = int(input())

says = []

for _ in range(N):
    A = int(input())
    say = [list(map(int, input().split())) for _ in range(A)]
    says.append(say)


# print(says)
max_upright_count = 0
for i in range(1 << N):
    integrate = True
    upright_count = 0
    declares = [-1 for _ in range(N)]
    for j in range(N):
        if not integrate:
            continue
        # もし真偽不明の場合は正しいことを言う場合もあるから無視する
        if (i >> j & 1) == 1:
            upright_count += 1
            for x, y in says[j]:
                # print(i, j, x, y, declares)
                if declares[x - 1] == -1:
                    declares[x - 1] = y
                else:
                    if declares[x - 1] == y:
                        continue
                    else:
                        integrate = False
                        break
    # print(bin(i), integrate, declares, upright_count)
    for j in range(N):
        # print((i >> j) & 1, declares[j])
        if ((i >> j) & 1) != declares[j] and declares[j] != -1:
            # print(False)
            integrate = False
    # print(integrate)
    if integrate:
        max_upright_count = max(max_upright_count, upright_count)
print(max_upright_count)
