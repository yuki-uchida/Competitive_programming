p = float(input())
EPS = 1e-8


def moore(x, p=p):
    return x + p / pow(2, x / 1.5)


def check_tilt(num):
    return moore(num + EPS) - moore(num)


left = 0
right = p

while right - left > EPS:
    mid = (left + right) / 2
    if check_tilt(mid) >= 0:
        right = mid
    else:
        left = mid

print(moore(left))
