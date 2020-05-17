N = int(input())
towns = [list(map(int, input().split())) for _ in range(N)]

# 全ての町の間に道を作りたい
# ただし、もっともお金がかからないように、最低限の道だけ作りたい
# また、もっともお金がかからない = もっとも近いなので、最短の経路を見つけ出せば良い。
# 全ての道を出して、そこから最小全域木出せば良さそう

loads = []
inf = float('inf')

for i in range(N):
    for j in range(i, N):
        loads.append([i, j, min(abs(towns[i][0] - towns[j][0]), abs(towns[i][1] - towns[j][1]))])
loads.sort(key=lambda x: x[2])
print(loads)

nodes = [i for i in range(N)]


def root(node):
    # 自身が根の場合はそのまま返す
    if nodes[node] == node:
        return node
    # 自身が根じゃない場合、現在自身の根と仮決めされているものの根をチェックして、修正する
    nodes[node] = root(nodes[node])
    return nodes[node]


cost = 0
for i, j, k in loads:
    if k == inf:
        continue
    # 根元を確認して、同じなら素通り
    # 違う根元のもののみ使う？
    print(i, j, root(i), root(j))
    # i = jの時は問答無用でpass
    if not root(i) == root(j):
        # 違う根元ならそのコストを追加する
        cost += k
        # iの根元をjの根元と同じにする。これによって新しく出てきたものは同じ根元になり追加しないようにする
        # なので事前にソートしておき、最小のもののみコストにたす
        nodes[root(i)] = root(j)
        print(nodes)
# print(nodes)
print(cost)
