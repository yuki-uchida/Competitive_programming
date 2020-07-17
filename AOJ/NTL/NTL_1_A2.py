import math
n = int(input())


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


print(str(n) + ":", *prime_factorization(n))
