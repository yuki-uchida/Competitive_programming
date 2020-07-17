from math import factorial
W, H = map(int, input().split())


mod = 10**9 + 7

ans = factorial(W + H - 2) // (factorial(H - 1) * factorial(W - 1))
print(ans % mod)