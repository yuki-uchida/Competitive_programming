N = int(input())
ans = N

# n = 6で取り出すお金
for n in range(N + 1):
    c = 0
    price_by_6 = n
    while price_by_6 > 0:
        c += price_by_6 % 6  # これを繰り返すと必要な回数になる。まず初回にあまりがある場合には1円が必要な分だけ足される。
        price_by_6 //= 6
    price_by_9 = N - n
    while price_by_9 > 0:
        c += price_by_9 % 9  # これを繰り返すと必要な回数になる。まず初回にあまりがある場合には1円が必要な分だけ足される。
        price_by_9 //= 9
    ans = min(ans, c)

print(ans)
