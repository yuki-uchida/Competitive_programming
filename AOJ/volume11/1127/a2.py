import queue
import math


def root(node):
    if nodes[node] == node:
        return node
    nodes[node] = root(nodes[node])
    return nodes[node]


while True:
    n = int(input())
    if n == 0:
        break

    cells = [list(map(float, input().split())) for _ in range(n)]

    nodes = [i for i in range(n)]

    q = queue.PriorityQueue()
    cost = 0
    count = n
    for i in range(n - 1):
        for j in range(i, n):
            d = math.sqrt((cells[i][0] - cells[j][0])**2 + (cells[i][1] - cells[j][1])**2 + (cells[i][2] - cells[j][2])**2)
            if d <= cells[i][3] + cells[j][3]:
                if root(i) != root(j):
                    nodes[root(i)] = root(j)
                    count += 1
            else:
                q.put((d - cells[i][3] - cells[j][3], i, j))
    while not q.empty():
        if count <= 1:
            break
        d, i, j = q.get()
        if root(i) != root(j):
            nodes[root(i)] = root(j)
            count -= 1
            cost += d
    print('{:.3f}'.format(cost))
