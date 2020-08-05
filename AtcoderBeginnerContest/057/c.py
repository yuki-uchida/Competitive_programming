import math
N = int(input())
# N = A*Bに変形したいが、A,Bの組み合わせはいくつかあるはず。
# 50なら、(1,50)(2,25)(5,10)(10,5)(25,2)(50,1)
# 基本的に、順に並べた時に真ん中にあるやつが一番A,Bの間に桁数の差がない。なのでこれを使えば最小値は求められそう。
# 7*7 < 50 < 8*8 なので、検索範囲はsqrt(50)まで。
# そうすると、1<=  N <= 10**10 なので、検索範囲を10**5まで減らせる。あとは全部やればいい


def f(a, b):
    return len(a) if len(a) >= len(b) else len(b)


ans = float('inf')
for a in range(1, int(math.sqrt(N)) + 1):
    if N % a != 0:
        continue
    b = int(N / a)
    a = str(a)
    b = str(b)
    # print(a, b)
    ans = min(ans, f(a, b))
print(ans)
