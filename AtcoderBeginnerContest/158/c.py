import math
A, B = list(map(int, input().split()))

A_min = math.ceil(A * 25 / 2)
A_max = ((A + 1) * 25 / 2)
if A_max > math.floor(A_max):
    A_max = math.floor(A_max) + 1
else:
    A_max = A_max
A_max = int(A_max)
B_min = B * 10
B_max = (B + 1) * 10
# print(B_min, B_max)
A_list = list(range(A_min, A_max))
B_list = list(range(B_min, B_max))
# print(A_list)
# print(B_list)

min_ans = -1
for num in A_list:
    if num in B_list:
        min_ans = num
        break
    else:
        continue

print(min_ans)
