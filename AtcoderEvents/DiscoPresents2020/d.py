M = int(input())
d = [0] * M
c = [0] * M
for i in range(M):
    d[i], c[i] = map(int, input().split())

# print(d)
# print(c)

D = 0
S = 0
for i in range(M):
    D += c[i]
    S += d[i] * c[i]

# print(D, S)
print((D - 1) + (S - 1) // 9)
