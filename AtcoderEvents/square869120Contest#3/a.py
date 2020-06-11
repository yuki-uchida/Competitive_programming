import copy
H, W, K = map(int, input().split())
nums = [list(map(int, list(input()))) for _ in range(H)]
ans = 0
for row in range(1, H):
    for col in range(W):
        score = 0
        iterations = 0
        squares = copy.deepcopy(nums)
        squares[row][col] = 0
        # print(squares)
        while True:
            not_falled = True
            # 下からやっていった方がいい。また、0行目はやる必要なし
            for i in range(H - 1, 0, -1):
                for k, num in enumerate(squares[i]):
                    if num == 0 and squares[i - 1][k] != 0:
                        squares[i - 1][k], squares[i][k] = squares[i][k], squares[i - 1][k]
                        not_falled = False
            if not_falled:
                break
        # print(squares)
        while True:
            deleted = False
            for i in range(H):
                for j in range(W, K - 1, -1):
                    for k in range(W - j + 1):
                        deletable = True
                        first_num = squares[i][k]
                        if first_num == 0:
                            continue
                        for num in squares[i][k + 1:k + j]:
                            if first_num != num:
                                deletable = False
                                break
                        # print(deletable)
                        if deletable:
                            # print((2**iterations) * (first_num * j))
                            score += (2**iterations) * (first_num * j)
                            squares[i][k:k + j] = [0] * j
                            deleted = True
            # print(squares)
            if deleted:
                while True:
                    not_falled = True
                    # 下からやっていった方がいい。また、0行目はやる必要なし
                    for i in range(H - 1, 0, -1):
                        for k, num in enumerate(squares[i]):
                            if num == 0 and squares[i - 1][k] != 0:
                                squares[i - 1][k], squares[i][k] = squares[i][k], squares[i - 1][k]
                                not_falled = False
                    if not_falled:
                        break
            else:
                break
            iterations += 1
        # print(ans, score)
        ans = max(ans, score)
print(ans)
# print(squares)s
