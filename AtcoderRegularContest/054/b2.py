P = float(input())
left = 0
right = 100
EPS = 1e-8

# 3分探索をする

mid = int((left + right) / 2)

# left < c1 < c2 < right
# これで、f(c1) > f(c2)だったら、c1よりに最大値があるはず
# right を c2に変更する
# これでc2 < f(c2)の領域を消せる。
# こうすると凸関数の答えを求められる。
# ３分探索は極値が一つしかないものを探索するアルゴリズム


def ternary_search(target, left_range, right_range):
    left = left_range
    right = right_range
    while abs(right - left) >= EPS:
        left_mid = left + (((right - left) / 3) * 1)
        right_mid = left + (((right - left) / 3) * 2)
        left_mid_speed = left_mid + (target / (2**(left_mid * 2 / 3)))
        right_mid_speed = right_mid + (target / (2**(right_mid * 2 / 3)))
        # print(left_mid, right_mid, left_mid_speed,
        #       right_mid_speed, left_mid_speed > right_mid_speed)
        if left_mid_speed > right_mid_speed:
            left = left_mid
        else:
            right = right_mid

    return left + (target / (2**(left * 2 / 3)))


print(ternary_search(P, left, right))
