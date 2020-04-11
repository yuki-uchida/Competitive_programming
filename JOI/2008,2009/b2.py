# -*- coding: utf-8 -*-
d = int(input())  # 2 <= d <= 10^9
n = int(input())  # 2 <= n <= 10^5
m = int(input())  # 1 <= m <= 10^4

# dを足せば円を直線状に表せる
store_positions = [0, d]

for _ in range(n - 1):
    store_positions.append(int(input()))
store_positions = sorted(store_positions)
destination_postions = []
for _ in range(m):
    destination_postions.append(int(input()))

# print(store_positions)
# print(destination_postions)


def binary_search(positions, num, left, right):
    if left > right:
        return left - 1
    mid = int((left + right) / 2)
    if positions[mid] < num:
        return binary_search(positions, num, mid + 1, right)
    elif positions[mid] == num:
        return mid
    else:
        return binary_search(positions, num, left, mid - 1)


# # print("===========")
total_cost = 0
for destination_postion in destination_postions:
    # print('start')
    index = binary_search(store_positions,
                          destination_postion, 0, n - 1)
    # print(index)
    cost = min(store_positions[index + 1] - destination_postion,
               destination_postion - store_positions[index])
    # print(index, cost)
    # if index == n:
    #     cost = min(abs(destination_postion - store_positions[index - 1]),
    #                abs(destination_postion - store_positions[index]))
    # else:
    #     cost = min(abs(destination_postion - store_positions[index]),
    #                abs(destination_postion - store_positions[index + 1]))
    total_cost += cost

print(total_cost)
