H, W, K, V = map(int, input().split())
# あらかじめ地価のK円は足しておく
land_prices = [[K for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(1, H + 1):
    row_land_prices = list(map(int, input().split()))
    for j in range(1, W + 1):
        land_prices[i][j] += land_prices[i - 1][j] + land_prices[i][j - 1] - land_prices[i - 1][j - 1] + row_land_prices[j - 1]
# print(land_prices)
# 選んだマスS個*K円が建設費用
# 持っているお金V円　
# 出来るだけ面積の大きい家を買いたい。マスによって地価が違うので、それも含めて一番安く一番広いものを選択する

# 選んだ領域(A1+...+As) + S*K
# 10**8
max_spaces = 0
for i_1 in range(1, H + 1):
    for i_2 in range(i_1, H + 1):
        for j_1 in range(1, W + 1):
            for j_2 in range(j_1, W + 1):
                cost = land_prices[i_2][j_2] - (land_prices[i_1 - 1][j_2] + land_prices[i_2][j_1 - 1] - land_prices[i_1 - 1][j_1 - 1])
                if cost > V:
                    continue
                # print(i_1, i_2, j_1, j_2, cost)
                spaces = (j_2 - j_1 + 1) * (i_2 - i_1 + 1)
                max_spaces = max(max_spaces, spaces)

print(max_spaces)
