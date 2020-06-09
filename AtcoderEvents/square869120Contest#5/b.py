# no_r_spheresの半径を求める。
# ただし、どの円とも交わらず、含んでいない。接することは許される。
# math.sqrt((y2-y1)**2 - (x2-x1)**2) >= r1+r2 である必要がある
# 半径を決めなければいけない円は複数ある。ただし、その中でもっとも半径が短いものの半径を最大化する
# 最大化 = 何かの円と接する必要がある

# 半径が決まっていない円を使って、すでに半径が決まっている円と接する、他の円と交わらない、もっとも長い半径は出すことができる

N, M = map(int, input().split())
circles = [tuple(map(int, input().split())) for _ in range(N)]
points = [tuple(map(int, input().split())) for _ in range(M)]


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def not_intersect(r1):
    for x1, y1 in points:
        for x2, y2, r2 in circles:
            if distance(x1, y1, x2, y2) < r1 + r2:
                return False
    return True


md = float('inf')
mr = float('inf')
for i in range(M):
    for j in range(M):
        if i == j:
            break
        a1, b1 = points[i]
        a2, b2 = points[j]
        md = min(md, distance(a1, b1, a2, b2) / 2)
# mdは半径が決まっていない円同士のもっとも短い距離/2

for i in range(N):
    mr = min(mr, circles[i][2])
# mrはすでに半径が決まっている円のもっとも短い半径

if N == 0:
    print(md)
    exit()
if M == 0:
    print(mr)
    exit()

left = 0
right = 1000
# 二分探索で、もっとも大きい半径を見つける
while right - left > 10**(-8):
    mid = (left + right) / 2
    # その半径を使ってみて交わらなかった場合、もっと長くできるのでleft = mid
    if not_intersect(mid):
        left = mid
    # 交わった場合にはもっと短くしてみたいので right = mid
    else:
        right = mid
print(min(left, md, mr))
