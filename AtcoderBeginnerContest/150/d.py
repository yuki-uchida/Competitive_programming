from fractions import gcd
# from math import gcd
from functools import reduce
N, M = map(int, input().split())
nums = set([num // 2 for num in list(map(int, input().split()))])
# 1<=X<=Mの範囲で、半公倍数の数を求める。
# 但し、Xは、num*(p+0.5)でなければならない
# Mが10**9なので、全部やるのは無理。
# n.5倍なので、numsのあたいは全て偶数になっている。

# nums一つ一つ、答えになりうるXの配列を作って、重複したものを残せばそれが答えになる。
# Nが10**5なので、どうだろう


def half_multiple(x, y):
    # 最大公約数は無駄なのではぶく
    # x=6,y=10なら=>2が無駄なもの
    return (x * y) // gcd(x, y)


def run():
    half_multiple_num = reduce(half_multiple, nums, 1)

    # print(half_multiple_num)
    for num in nums:
        # n.5倍の値でなければならないので、ここでチェックする
        if (half_multiple_num // num) % 2 == 0:
            print(0)
            return

    ans = M // half_multiple_num
    ans = ans - 1 if ans % 2 == 0 else ans

    print((ans + 1) // 2)


run()
