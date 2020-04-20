D, N = map(int, input().split())
temperatures = []
clothes = []

for _ in range(D):
    temperatures.append(int(input()))
for _ in range(N):
    clothes.append(list(map(int, input().split())))

# print(temperatures)
# print(clothes)
inf = float('inf')
# D = スケジュールを立てないといけない日数
dps = [[-inf for _ in range(N)] for _ in range(D)]


for i in range(D):
    temperature = temperatures[i]
    for j in range(N):
        a, b, c = clothes[j]
        if a <= temperature <= b:
            if i == 0:
                dps[i][j] = 0
            else:
                for k in range(N):
                    _, _, pre = clothes[k]
                    dps[i][j] = max(dps[i][j], abs(c - pre) + dps[i - 1][k])
# print(dps)
print(max(dps[D - 1]))
