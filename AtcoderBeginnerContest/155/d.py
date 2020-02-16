N, K = input().split(" ")

nums = input().split(" ")
nums = [int(n) for n in nums]

products = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        products.append(nums[i] * nums[j])
# 3重for文にするとか


def merge(array):                                   # line1155
    mid = len(array)                                # line2
    if mid > 1:
        half = int(mid / 2)                        # line3
        left = merge(array[:half])               # line4
        right = merge(array[half:])              # line5
        array = []                                  # line6
        while len(left) != 0 and len(right) != 0:   # line7
            if left[0] < right[0]:                  # line8
                array.append(left.pop(0))           # line9
            else:                                   # line10
                array.append(right.pop(0))          # line11
        if len(left) != 0:                          # line12
            array.extend(left)                      # line13
        elif len(right) != 0:                       # line14
            array.extend(right)                     # line15
    return array


print(merge(products)[int(K) - 1])
