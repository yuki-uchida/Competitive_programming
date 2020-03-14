import math
H, W = list(map(int, input().split()))

total = H * W
if(H > 1 and W > 1):
    print(math.ceil(total / 2))
else:
    print(1)
