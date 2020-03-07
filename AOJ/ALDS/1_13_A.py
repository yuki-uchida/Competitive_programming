from itertools import permutations

N = 8

M = [['.'] * N for i in range(N)]
# print(M)
A0 = set()
B0 = set()

K = int(input())
R = set(range(N))
C = set(range(N))
for i in range(K):
    r, c = map(int, input().split())
    R.remove(r)
    C.remove(c)
    M[r][c] = 'Q'
    A0.add(r + c)
    B0.add(r - c)
# print(A0)
# print(R)
# print(C)

# print(list(permutations(C)))
# A0,B0は、同じ斜め列の判別に使う。


# 使える列(C.remove(c))から全ての順列をだす。
for CS in permutations(C):
    A = A0.copy()
    B = B0.copy()
    ok = 1
# その列の順列と、行を同時にzip関数で開く
    for r, c in zip(R, CS):
        # 斜めチェック(↙︎)
        if r + c in A:
            ok = 0
        A.add(r + c)
# 斜めチェック(↘︎)
        if r - c in B:
            ok = 0
        B.add(r - c)
    if ok:
        for r, c in zip(R, CS):
            M[r][c] = 'Q'
        break
print(*("".join(m) for m in M), sep='\n')
