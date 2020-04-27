while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    # 区間DP
    # dps[i][r]を更新する際に、
    # dps[i][k] dps[k+1][r]までの数を確認して、大きい方を使う。
    # 今回は、i~rまでのkを全て確認して更新する

    dps = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if j - i == 1:
                if abs(nums[i] - nums[j]) <= 1:
                    dps[i][j] = 2
            else:
                for k in range(i + 1, j):
                    # if i == 0:
                    #     print(i, k, j)
                    dps[i][j] = max(dps[i][j], dps[i][k] + dps[k + 1][j])
                if abs(nums[i] - nums[j]) <= 1 and dps[i + 1][j - 1] == ((j - 1) - (i + 1) + 1):
                    dps[i][j] = max(dps[i][j], dps[i + 1][j - 1] + 2)
    print(dps[0][n - 1])
