import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# print(graph)
v = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    v[p - 1] += x
# print(v)


seen_points = [True] * N
seen_points[0] = False
stack = [0]

while stack:
    now = stack.pop()
    for i in graph[now]:
        if seen_points[i]:
            seen_points[i] = False
            stack.append(i)
            v[i] += v[now]

print(*v)
