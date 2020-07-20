from itertools import accumulate
from bisect import bisect_right, bisect_left
# Kは読める時間。この時間を最大に使ってたくさん本を読みたい
N, M, K = map(int, input().split())

a_books = list(map(int, input().split()))
b_books = list(map(int, input().split()))
a_books = list(accumulate(a_books))
b_books = list(accumulate(b_books))
a_books.insert(0, 0)
b_books.insert(0, 0)
a_index = bisect_right(a_books, K)

# print(a_books)
# print(b_books)


max_nums = 0
for i in range(a_index):
    a_cost = a_books[i]
    remain_cost = K - a_cost
    if remain_cost < 0:
        continue
    j = bisect_right(b_books, remain_cost)
    # print(i, j)
    max_nums = max(max_nums, i + j - 1)
print(max_nums)
