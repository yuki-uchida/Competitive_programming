n = int(input())
k = int(input())
mod = 10**9 + 7

# a**bのmodを取りたい時に高速にできる


def modpow(a, n, mod):
    res = 1
    # 45 = 101101
    # ここでいう、1X11X1の部分飲み計算すれば良い
    # a**45 = a**32 + a**8 + a**4 + a**1なので、これだけ計算すれば良い
    # そしてそのためには、45を2進数に変えて、右ビットシフトしていけばok
    # なので、n >>= 1をする
    # ex)45,22,11,5,2,1
    while (n > 0):
        # print(n, a, res)
        # 3&1みたいな論理積とった結果、両方1のものがあった場合にresにたす
        if n & 1:
            res = res * a % mod
        # a = 掛け算の結果を更新する。
        # a*b の mod(c)は。a mod(c)*b mod(c)と同じなので、掛け算するaもmodをとっていく
        a = a * a % mod
        # n>>1で、1桁ずつ減らしていく
        # 101101 > 10110みたいな
        # 先頭の1文字が減るわけではない。45->45-32みたいな感じではない
        # でも、やりたいのは、1X11X1の部分のみ計算するための、右bitシフトなので45->22の部分に特に意味はない
        # 101101 > 10110をすることで末尾が一つずつ消していけることが重要
        # n=n>>1をすることで二進法展開ができる
        n = n >> 1
    return res


def solve(n, r, mod):
    # 1<=a1<=a2<=...<=ak<=nであるような整数の組を計算する
    # n=10 k=2なら 1<=a1<=a2<=10の整数の組を計算する
    # n種類のものから重複を許してr個選ぶ場合の数はn+r-1Cr通り
    # hCr = hPr / rPr
    # hPr = n+r-1Pr
    # rPr
    h = n + r - 1
    hPr, rPr = 1, 1
    for i in range(r):
        hPr = hPr * (h - i) % mod
        rPr = rPr * (i + 1) % mod
    return (hPr * modpow(rPr, mod - 2, mod)) % mod


print(solve(n, k, mod))


# nCrの形まで持っていきたい
