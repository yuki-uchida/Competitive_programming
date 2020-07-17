import math
Q = int(input())


def prime_factorization(num):
    sqrt_num = math.sqrt(num)
    prime_numbers = []
    for i in range(2, int(sqrt_num) + 1):
        # print(num)
        while num % i == 0:
            # print(num)
            num = num / i
            prime_numbers.append(i)
    if num != 1:
        prime_numbers.append(int(num))
    return prime_numbers


for i in range(Q):
    l, r = map(int, input().split())
    count = 0
    for k in range(l, r + 1):
        if k % 2 == 1:
            # print(k)
            if len(prime_factorization(k)) == 1 and len(prime_factorization((k + 1) // 2)) == 1:
                count += 1
    print(count)
