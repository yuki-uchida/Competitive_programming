N = int(input())

areas = [list(input()) for _ in range(5)]
# その列の５ますが全て全部青・白・赤のいずれかであり、どの隣り合った二つの列も色が異なる状態にしたい。
# 黒はだめ
# 最小で幾つのマス塗り替える必要があるかを求めるプログラムを描きたい
inf = float('inf')
dps = [[inf for _ in range(3)] for _ in range(N)]

# print(areas)
for i in range(N):
    for j in range(3):
        colors = ['R', 'B', 'W']
        if i == 0:
            color = colors[j]
            cost = 0
            for k in range(5):
                if areas[k][i] != color:
                    cost += 1
            dps[i][j] = cost
        else:
            color = colors[j]
            # colors.pop(color)
            cost = 0
            for k in range(5):
                # print(areas[k][i], color)
                if areas[k][i] != color:
                    cost += 1
            # print(i, j, color, cost)
            dps[i][j] = min(dps[i - 1][j - 2] + cost, dps[i - 1][j - 1] + cost)

print(min(dps[N - 1]))
