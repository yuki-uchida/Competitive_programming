from math import factorial
W, H = map(int, input().split())
# 0,0からW-1,H-1まで行く経路の個数
mod = 10**9 + 7
ans = factorial(W + H - 2) // (factorial(H - 1) * factorial(W - 1))
print(ans % mod)
