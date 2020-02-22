n, a, b = list(map(int, input().split(" ")))
mod = 1000000007

# flowers = [i for i in range(1, n + 1)]
# 4 1 3
# 2^4 - 1 - 4C1 - 4C3


def modpow(a, n, mod):
    res = 1
    while (n > 0) {
        if (n & 1) res = res * a % mod
        a = a * a % mod
        n >>= 1
    }
    return res


}

total = modpow(2, n, mod)
# nCa = n! / a!
# nCb = n! / b!

# 0の時も考える
nPa = 1
nPb = 1
aPa = 1
bPb = 1
for i in range(n - a + 1, n + 1):
    nPa = (nPa * i) % mod
for i in range(n - b + 1, n + 1):
    nPb = (nPb * i) % mod
for i in range(2, a + 1):
    aPa = (aPa * i) % mod
for i in range(2, b + 1):
    bPb = (bPb * i) % mod
print(nPa)
print(nPb)
print(aPa)
print(bPb)
nCa = (nPa / aPa) % mod
nCb = (nPb / bPb) % mod
print(int(total - 1 - nCa - nCb))
