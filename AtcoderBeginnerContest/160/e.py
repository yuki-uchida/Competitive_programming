
from bisect import bisect_left
X, Y, A, B, C = map(int, input().split())
red_apples = list(map(int, input().split()))
green_apples = list(map(int, input().split()))
white_apples = list(map(int, input().split()))
# while_applesから、どれを赤に、緑にするか。
# とりあえず無色のままにする必要はないので、0=赤1=緑として、white_applesを全て振り分けてみる
# その全ての組み合わせを探索する？


max_cost = 0
for i in range(2**C):
    to_red_apples = []
    for j in range(C):
        if((i >> j) & 1):
            to_red_apples.append(1)
        else:
            to_red_apples.append(0)
    new_red_apples = []
    new_red_apples.extend(red_apples)
    new_green_apples = []
    new_green_apples.extend(green_apples)
    for index, apple in enumerate(white_apples):
        if to_red_apples[index] == 1:
            new_red_apples.append(apple)
        else:
            new_green_apples.append(apple)
    new_red_apples.sort(reverse=True)
    new_green_apples.sort(reverse=True)
    cost = 0
    for i in range(X):
        cost += new_red_apples[i]
    for i in range(Y):
        cost += new_green_apples[i]
    max_cost = max(max_cost, cost)
print(max_cost)
