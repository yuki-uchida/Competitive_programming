from itertools import accumulate
INF = float('inf')


def prime_numbers(n):
    if n < 2:
        return []

    m = (n + 1) // 2
    p = [True] * m
    for i in range(1, int((n ** 0.5 - 1) / 2) + 1):
        if p[i]:
            for j in range(2 * i * (i + 1), m, 2 * i + 1):
                p[j] = False

    a = [2 * i + 1 for i in range(m) if p[i]]
    a[0] = 2
    return a


N = 10 ** 5
P = set(prime_numbers(N))
# これが素数
print(P)
P = [n for n in P if (n + 1) // 2 in P]
# 自身 + 1 //2 も素数であるもののみに絞る
print(P)
a = [0] * (N + 1)
for n in P:
    # likenumberは1にする
    a[n] = 1
# 累積和に変換
a = list(accumulate(a))


Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(a[r] - a[l - 1])
