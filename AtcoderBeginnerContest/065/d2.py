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

# グラフの各頂点がそれぞれの木に属するように、木を作成する。
# 最初は自身のみを入れておく
nodes = [i for i in range(N)]
# sizes = [1 for _ in range(N)]


def find(x):
    if x == nodes[x]:
        return x
    nodes[x] = find(nodes[x])
    return nodes[x]


def unite(x, y):
    root_x = find(x)
    root_y = find(y)
    # すでに同じ木に属している(同じ根を持っている)ならマージしない
    if root_x == root_y:
        return
    # if sizes[root_x] < sizes[root_y]:
    #     sizes[root_x] = sizes[root_y]
    # xの根がyの根の親になるように連結する
    nodes[root_y] = root_x
    # sizes[root_x] += sizes[root_y]


def same(x, y):
    return find(x) == find(y)


# def size(x):
#     return sizes[find(x)]


cost = 0
for i, j, k in loads:
    # 根元を確認して、同じなら素通り
    # 違う根元のもののみ使う？
    # i = jの時は問答無用でpass
    print(i, j, same(i, j))
    if not same(i, j):
        # 違う根元ならそのコストを追加する
        cost += k
        # iの根元をjの根元と同じにする。これによって新しく出てきたものは同じ根元になり追加しないようにする
        # なので事前にソートしておき、最小のもののみコストにたす
        unite(i, j)
        print(nodes)
# print(nodes)
print(cost)
