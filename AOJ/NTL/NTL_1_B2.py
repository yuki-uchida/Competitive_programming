m, n = map(int, input().split())
mod = 10**9 + 7


def modpow(m, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * m % mod
        m = m * m % mod
        n >>= 1
    return res


print(modpow(m, n, mod))
