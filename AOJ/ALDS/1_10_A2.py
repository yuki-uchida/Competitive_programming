n = int(input())


dps = [0 for _ in range(n + 1)]

dps[0] = 1
dps[1] = 1

for i in range(2, n + 1):
    dps[i] = dps[i - 2] + dps[i - 1]

print(dps[n])
