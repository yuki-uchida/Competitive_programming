from collections import deque
import math
N = int(input())
# 以下の条件を全て満たすzを選ぶ
# ある素数pと正の整数eを用いてz=p**eと表すことができる
# Nがzで割り切れる
# 以前の操作で使ったものは使えない

# これを、N=N/zで繰り返し行い、何回行えるかを出力する

used_nums = deque([1])


def prime_numbers(n):
    if n < 2:
        return []

    m = (n + 1) // 2
    p = [True] * m
    for i in range(1, int((n ** 0.5 - 1) / 2) + 1):
        if p[i]:
            for j in range(2 * i * (i + 1), m, 2 * i + 1):
                p[j] = False
    # 素数のみ返す
    a = [2 * i + 1 for i in range(m) if p[i]]
    a[0] = 2
    return a


P = set(prime_numbers(math.ceil(math.sqrt(10**12))))
# これが素数
P = [n for n in P if (N % n) == 0]
# Nを割り切れるもののみのこす
# print(P)
for num in P:
    start_x = 1
    while N >= num**start_x:
        if N % num**start_x != 0:
            start_x += 1
            continue
        if N % (num**start_x) == 0:
            N = int(N / (num**start_x))
            used_nums.append(num**start_x)
        start_x += 1
# print(N)
# print(used_nums)
if N not in used_nums:
    used_nums.append(N)
print(len(used_nums) - 1)
