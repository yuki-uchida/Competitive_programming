N = int(input())
# nums = [i for i in range(1, N + 1)]
if (N - 1) % 2 == 0:
    print(N * ((N - 1) // 2))
else:
    # 12 =>
    print(N * ((N - 1) // 2) + (N // 2))
