import bisect
n = int(input())

nums = [int(input()) for _ in range(n)]

LIS = [nums[0]]

# for i in range(n):
#     if nums[i] > LIS[-1]:
#         LIS.append(nums[i])
#     else:
#         LIS[bisect.bisect_left(LIS, nums[i])] = nums[i]

for num in nums:
    if num > LIS[-1]:
        LIS.append(num)
    else:
        LIS[bisect.bisect_left(LIS, num)] = num
    print(LIS)


print(LIS)
print(len(LIS))


# この書き方は、長さがわかれば良いので、2341みたいな形で出てきた時、LIS[0]に1が入るようになっている。
# ただし、これによって先頭を初期化しつつ、次の値を入れていくことができる。
# そして、過去に出た文字列の最も長かったものの長さも配列の長さから取得できる。
# 最長部分文字列を文字列で欲しい場合にはこの書き方ではダメ
# 6
# 5
# 2
# 4
# 4
# 5
# 1
# [5]
# [2]
# [2, 4]
# [2, 4]
# [2, 4, 5]
# [1, 4, 5]
# [1, 4, 5]
# 3
