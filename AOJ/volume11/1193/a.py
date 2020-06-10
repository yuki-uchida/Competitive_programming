while True:
    H = int(input())
    if H == 0:
        break
    squares = [list(map(int, input().split())) for _ in range(H)]
    score = 0
    while True:
        deleted = False
        for i in range(H):
            for j in range(5, 2, -1):
                for k in range(5 - j + 1):
                    deletable = True
                    first_num = squares[i][k]
                    if first_num == 0:
                        continue
                    for num in squares[i][k + 1:k + j]:
                        if first_num != num:
                            deletable = False
                            break
                    if deletable:
                        score += first_num * j
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
    print(score)
    # print(squares)
