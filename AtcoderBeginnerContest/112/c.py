N = int(input())

high_sets = [list(map(int, input().split())) for _ in range(N)]

# このセットから中心座標と高さは絞り込める


def compute_diff_from_top(x, y, cx, cy):
    # -4 + -77
    return ((-1 * abs(x - cx)) + (-1 * abs(y - cy)))


ans = 0
ans_x = None
ans_y = None
for i in range(101):
    for j in range(101):
        nums = []
        for high_set in high_sets:
            # i == 55 j == 80
            # high_set_x = 59 high_set_y = 3
            # high_set[2] == 0の時は、区別が必要。
            num = high_set[2] + (-1 * compute_diff_from_top(i, j, high_set[0], high_set[1]))
            if high_set[2] == 0:
                nums.append(-1)
            else:
                nums.append(num)
        # if i == 32:
        #     print(i, j, nums)
        if len(set(nums)) == 1:
            ans_x, ans_y = i, j
            ans = nums.pop()
        else:
            if len(set(nums)) == 2 and -1 in nums:
                nums = set(nums)
                nums.remove(-1)
                top = nums.pop()
                check = True
                for high_set in high_sets:
                    # if i == 32 and j == 68:
                    #     print(top, compute_diff_from_top(i, j, high_set[0], high_set[1]))
                    if max(0, top + compute_diff_from_top(i, j, high_set[0], high_set[1])) != high_set[2]:
                        check = False
                if check:
                    ans_x, ans_y = i, j
                    ans = top


print(ans_x, ans_y, ans)
# 55 80 79
