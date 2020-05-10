V, E = map(int, input().split())
inf = float('inf')
dps = [[inf for _ in range(V)] for _ in range(V)]
for _ in range(E):
    node_a, node_b, cost = map(int, input().split())
    dps[node_a][node_b] = cost
# print(dps)


for i in range(V):
    dps[i][i] = 0
for k in range(V):
    for i in range(V):
        for j in range(V):
            dps[i][j] = min(dps[i][j], dps[i][k] + dps[k][j])

flag = False
for i in range(V):
    if dps[i][i] < 0:
        flag = True

if flag:
    print('NEGATIVE CYCLE')
else:
    for dp in dps:
        print(*['INF' if num == inf else num for num in dp])
