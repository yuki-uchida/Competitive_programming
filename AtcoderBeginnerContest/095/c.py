A, B, C, X, Y = map(int, input().split(" "))

prices = []
if X > Y:
    half_max_count = X + 1
else:
    half_max_count = Y + 1

# 3 for文はダメなので削減する
# sliceで半分にできる多分。
for i in range(0, half_max_count):
    a_price = int(X - i) * A if (int(X - i) >= 0) else 0
    b_price = int(Y - i) * B if (int(Y - i) >= 0) else 0
    half_price = 2 * i * C
    price = half_price + a_price + b_price
    prices.append(price)
print(min(prices))
