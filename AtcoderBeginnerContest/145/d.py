mod = 10 ** 9 + 7


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(cmb(n, r, p))


def main():
    X, Y = map(int, input().split())
    n = (-X + 2 * Y) / 3
    m = (2 * X - Y) / 3
    # これで(i+1,j+2)をとる回数がn回(i+2,j+1)をとる回数がm回だとわかる
    # 少数が出てきたら計算できないので0を返す
    if not(n.is_integer() and m.is_integer()):
        return 0
    if n >= 0 and m >= 0:
        # n+mCnを計算する。modを高速にとる
        return COM(int(n + m), int(n))
    else:
        return 0


# print(main())
