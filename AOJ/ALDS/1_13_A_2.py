from itertools import permutations
k = int(input())


# 8*8行の間で何行目に何があるか
start_exists = [[] for _ in range(8)]
exists_rows = []
for _ in range(k):
    r, c = map(int, input().split())
    exists_rows.append(r)
    start_exists[r].append(c)

# print(start_exists)


def check_valid_positions(exist_positions):
    valid = True
    for start_position in exist_positions:
        for check_position in exist_positions:
            if start_position == check_position:
                continue
            if start_position[0] == check_position[0]:
                valid = False
            if start_position[1] == check_position[1]:
                valid = False
            if (start_position[0] - start_position[1]) == (check_position[0] - check_position[1]):
                valid = False
            if (start_position[0] + start_position[1]) == (check_position[0] + check_position[1]):
                valid = False
    return valid


# これですでに存在している行は除く
# [(7, 6, 5, 2, 1, 3, 4, 0), (7, 6, 5, 2, 1, 4, 0, 3)....]
queens_row_permutations = permutations(range(8))
ans = []
for queens_row_permutation in queens_row_permutations:
    exist_positions = []
    for i, row in enumerate(queens_row_permutation):
        if i in exists_rows:
            exist_positions.append([i, start_exists[i][0]])
        else:
            exist_positions.append([i, row])
    # print(exist_positions)
    # print(check_valid_positions(exist_positions))
    if check_valid_positions(exist_positions):
        ans = exist_positions
        break
    # squares = [[0 for _ in range(8)] for _ in range(8)]
    # for i, row in enumerate(queens_row_permutation):
    #     if i in exists_rows:
    #         squares[i][start_exists[i][1]] = 1
    #     else:
    #         squares[i][row] = 1
    # for j in range(8):
for position in ans:
    print(
        ''.join(['Q' if position[1] == i else '.' for i in range(8)]))
