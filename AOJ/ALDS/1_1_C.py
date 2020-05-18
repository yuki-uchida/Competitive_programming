import math
n = int(input())
input_nums = [int(input()) for _ in range(n)]

primes = []
for i in range(2, 10000):
    is_prime = True
    # 今まででた素数で割っていくと、自身が素数かどうかわかる
    for p in primes:
        if i % p == 0:
            is_prime = False
    if is_prime:
        primes.append(i)


def check(n):
    for p in primes:
        # 全てprimesを見るのは時間が勿体無いので、自身よりも大きいもの・もしくは同じになったら抜ける.
        # もし素数でないのであれば、p<nの間にあるはず。ない状態で、同じ数値まで来た場合も素数
        if n <= p:
            return True
        if n % p == 0:
            return False
    return True


count = 0
for num in input_nums:
    if check(num):
        count += 1
print(count)
