from itertools import accumulate
H, W, K = map(int, input().split())
squares = [list(input()) for _ in range(H)]
# black_squares = []
# for i in range(H):
#     accumrated_list = []
#     for j, color in enumerate(list(input())):
#         if color == '#':
#             accumrated_list.append(1)
#         else:
#             accumrated_list.append(0)
#     accumrated_list = list(accumulate(accumrated_list))
#     black_squares.append(accumrated_list)
# print(black_squares)
# black_count = 0
# for i in range(H):
#     black_count += black_squares[i][W - 1]

# print(black_count)
# 2,3のエリアで、
# 消すところが0,0の場合、1,1から
ans = 0
for hs in range(1 << H):
    for ws in range(1 << W):
        # ここまででどの行と列を使うかが決まる。
        # 使用する行と列に含まれる黒の数をカウントする
        count = 0
        for i in range(H):
            for k in range(W):
                if hs >> i & 1 and ws >> k & 1:
                    # そこは使うのでカウントする
                    # print(hs >> i, ws >> k)
                    if squares[i][k] == '#':
                        count += 1
        if count == K:
            ans += 1
print(ans)
