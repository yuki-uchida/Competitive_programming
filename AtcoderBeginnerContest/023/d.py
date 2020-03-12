import itertools
N = int(input())
heights = []

for i in range(N):
    heights.append(list(map(int, input().split())))


max_height = sorted([num[0] + (num[1] * (N - 1)) for num in heights])

# print(max_height)


# def check_can_make(num, num_list):
#     limits = []
#     for height, speed in num_list:
#         limit = (num - height) / speed
#         if limit < 0:
#             return False
#         else:
#             limits.append(limit)
#     for i in range(len(num_list)):
#         if min(limits) >= i:
#             limits.remove(min(limits))
#         else:
#             return False
#     return True


# def left_binary_search(num_list, left, right):
#     if left > right:
#         return left
#     mid = (left + right) // 2
#     if check_can_make(mid, num_list):
#         return left_binary_search(num_list, left, mid - 1)
#     else:
#         return left_binary_search(num_list, mid + 1, right)


# print(left_binary_search(heights, min(max_height), max(max_height)))

left = min(max_height)
right = max(max_height)
while left <= right:
    mid = (left + right) // 2
    limits = []
    can_make = True
    for height, speed in heights:
        limit = (mid - height) // speed
        if limit < 0:
            can_make = False
            break
        else:
            limits.append(limit)
    limits = sorted(limits)
    for i in range(len(limits)):
        if limits[i] < i:
            can_make = False
            break
    if can_make:
        right = mid - 1
    else:
        left = mid + 1
print(left)
