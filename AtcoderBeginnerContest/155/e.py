# 一個上の桁まで計算すればおk。11なら、999まで？
# 違う。11なら、111まで


def main():
    N = [int(x) for x in input()]
    l = len(N) + 1
    DP = [[0] * 2 for _ in range(l)]
    DP[0][1] = 1
    for i, n in enumerate(N):
        DP[i + 1][0] = min(DP[i][0] + n, DP[i][1] + (10 - n))
        DP[i + 1][1] = min(DP[i][0] + (n + 1), DP[i][1] + (10 - (n + 1)))
    print(DP[-1][0])


if __name__ == '__main__':
    main()
