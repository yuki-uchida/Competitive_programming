V, E = map(int, input().split())
inf = float('inf')
dps = [[inf for _ in range(V)] for _ in range(V)]

for _ in range(E):
    s, t, d = map(int, input().split())
    dps[s][t] = d


for i in range(V):
    dps[i][i] = 0
for v in range(V):
    for i in range(V):
        for j in range(V):
            dps[i][j] = min(dps[i][j], dps[i][v] + dps[v][j])
# print(dps)
flag = False
for i in range(V):
    if dps[i][i] < 0:
        flag = True
if flag:
    print('NEGATIVE CYCLE')
else:
    for dp in dps:
        print(*['INF' if num == inf else num for num in dp])
