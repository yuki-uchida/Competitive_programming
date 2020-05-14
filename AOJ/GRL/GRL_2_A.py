V, E = map(int, input().split())
inf = float('inf')
graphs = [list(map(int, input().split())) for _ in range(E)]
graphs.sort(key=lambda x: x[2])

nodes = [i for i in range(V)]
cost = 0


def root(node):
    if nodes[node] == node:
        return node
    nodes[node] = root(nodes[node])
    return nodes[node]


for i, j, k in graphs:
    if not root(i) == root(j):
        cost += k
        nodes[root(i)] = root(j)
print(cost)
