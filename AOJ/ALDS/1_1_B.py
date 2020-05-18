x, y = map(int, input().split())


def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if x % y == 0:
        return y
    return gcd(y, x % y)


print(gcd(x, y))
