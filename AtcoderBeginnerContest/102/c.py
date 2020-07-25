
import math
N = int(input())

A = list(map(int, input().split()))


B = sorted([a - i for i, a in enumerate(A, start=1)])

ans = []

if N % 2 == 1:
    b = B[N // 2]
    ans.append(sum([abs(x - b) for x in B]))
else:
    b_left = (B[N // 2 - 1] + B[N // 2]) // 2
    b_right = math.ceil((B[N // 2 - 1] + B[N // 2]) / 2)
    ans.append(sum([abs(x - b_left) for x in B]))
    ans.append(sum([abs(x - b_right) for x in B]))

print(min(ans))
