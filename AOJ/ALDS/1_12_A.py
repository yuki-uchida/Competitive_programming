n = int(input())
inf = float('inf')
graphs = []

for i in range(n):
    weights = list(map(int, input().split()))
    weights = [inf if weight == -1 else weight for weight in weights]
    graphs.append(weights)
# print(graphs)
# M =graphs

# WHITEは未訪問 BLACKは訪問済み
color = ['WHITE' for _ in range(n)]
d = [inf for _ in range(n)]
# 各点が所属する木の親を記録する
parents = [i for i in range(n)]
print(d)
print(parents)


def prim(start):
    # start地点を0で初期化する。[0,inf,inf,inf,inf]
    # 集合Tを更新しながら、まだ行ってない各点へ行くときのコストを更新し続ける。原点からのコストではなく、すでに到達済みの集合から次の点へ行くときの最小コストを更新する
    d[start] = 0
    # start地点の親はないので-1を記録しておく
    parents[start] = -1
    while True:
        min_cost = inf
        # 各頂点の色を確認する。そして、その各点が訪問済みでないもののみとする。
        # また、それが存在すること != inf
        # その中で、最短のd[i]を選んでそれを頂点として選ぶ。
        # 集合Tから移動する点を選ぶ。その際にもっとも低いコストのものを選ぶ
        for i in range(n):
            if color[i] != 'BLACK' and d[i] < min_cost:
                min_cost = d[i]
                u = i
        # 行けるところがないので終了する
        if min_cost == inf:
            break
        # 集合Tから次に行く点としてもっともコストが低いものへ移動する。そして訪問済みとする
        color[u] = 'BLACK'

        # その点uから各点をチェック
        for v in range(n):
            # すでに到達済み、もしくは辺がない場合は次へ
            if color[v] == 'BLACK' or graphs[u][v] == inf:
                continue
            # その点へ進む際に、u->vへの移動が、今まで記録されている、集合Tからvへ移動するコストよりも低い場合には移動する。
            # 低くない場合には、他の点から移動したほうがコストが低いということ
            if graphs[u][v] < d[v]:
                d[v] = graphs[u][v]
                # 最小コストで最小全域木を作れるときの、親を記録している
                parents[v] = u
                # この点は行けるので、'GRAY'にしてその点を次の移動先候補とする
                color[v] = 'GRAY'


prim(0)
print(d)
print(parents)
print(sum(d))
