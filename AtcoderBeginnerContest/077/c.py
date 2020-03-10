import bisect
N = int(input())
# サイズが下の方が大きくないとダメtop<mid<bottom
tops = sorted(list(map(int, input().split(" "))))
mids = list(map(int, input().split(" ")))
bottoms = sorted(list(map(int, input().split(" "))))
# print(tops)
# print(mids)
# print(bottoms)


# def left_binary_search(check_list, num, left, right):
#     if left > right:
#         return left
#     mid = (left + right) // 2
#     if check_list[mid] >= num:
#         return left_binary_search(check_list, num, left, mid - 1)
#     else:
#         return left_binary_search(check_list, num, mid + 1, right)


# def right_binary_search(check_list, num, left, right):
#     if left > right:
#         return left
#     mid = (left + right) // 2
#     if check_list[mid] > num:
#         return right_binary_search(check_list, num, left, mid - 1)
#     else:
#         return right_binary_search(check_list, num, mid + 1, right)


total_count = 0
for mid in mids:
    # bottom_start_index = right_binary_search(bottoms, mid, 0, N - 1)
    bottom_start_index = bisect.bisect_right(bottoms, mid)
    # top_end_index = left_binary_search(tops, mid, 0, N - 1)
    top_end_index = bisect.bisect_left(tops, mid)
    total_count += ((N - bottom_start_index) * top_end_index)
print(total_count)
