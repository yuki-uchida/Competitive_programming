N = int(input())
tops = list(map(int, input().split()))
middles = list(map(int, input().split()))
bottoms = list(map(int, input().split()))
tops.sort()
middles.sort()
bottoms.sort()
# print(tops)
# print(middles)
# print(bottoms)
# top<middle<bottomでないといけない
# middleをfor文で繰り返して、topとbottomで二分探索をする。
# そしてそれ以下の数を出して、掛け算すれば組み合わせの数を出せる


def left_binary_search(target, nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        # 0+7 /2 = 3
        # print(left, right)
        mid = int((left + right) / 2)
        # print(f'mid: {mid}')
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid - 1

    # 0,1,2,3,4
    # 2
    # => return 2
    # print(left, right)
    return left


def right_binary_search(target, nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        # 0+7 /2 = 3
        # print(left, right)
        mid = int((left + right) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # 0,1,2,3,4
    # 2
    # => return 2
    # print(left, right)
    return left


count = 0
for middle in middles:
    top_index = left_binary_search(middle, tops)
    bottom_index = right_binary_search(middle, bottoms)
    # print(top_index, bottom_index, (top_index) * (len(bottoms) - bottom_index))
    count += (top_index) * (len(bottoms) - bottom_index)
print(count)
