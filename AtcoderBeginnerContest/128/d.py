N, K = map(int, input().split())
values = list(map(int, input().split()))

# 1<=N<=50
# 1<=K<=100
# 10**8になってしまうので、全探索は無理そう？？？？


# CDは最後に持ってくれば良い。途中でやる必要はない
# A,Bをそれぞれ何回やるか決めれば、価値はわかるのでは。ただし、A,Bの数を合わせてKにならない場合もあり、その場合はリリースしないといけない
ans = 0

for i in range(K + 1):
    for j in range(K - i + 1):
        # 抜き出す動作がNを超えてしまった時、入れて取り出すという作業によって暇つぶしをする必要がある。
        # print(i, j, release_count)
        # i + j + relase_count = K
        for k in range(K - i - j + 1):
            if i + j < N:
                left_nums = values[0:i].copy()
                right_nums = values[N - j:N].copy()
                nums = sorted(left_nums + right_nums)
                ans = max(ans, sum(nums[k:]))
            elif i + j == N:
                nums = sorted(values.copy())
                ans = max(ans, sum(nums[k:]))
            else:
                if k < N - (i + j):
                    continue
                nums = sorted(values.copy())
                ans = max(ans, sum(nums[k - (N - (i + j)):]))


print(ans)
