
A, B, N = map(int, input().split())
# xはN以下
# int(A*x/B) - A*int(x/B)の最大値を求めたい


# print(compute_range)


def h(x):
    return int(int((A * x) / B) - A * int(x / B))


max_num = h(min(B - 1, N))
print(max_num)
