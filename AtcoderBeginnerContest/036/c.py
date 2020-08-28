N = int(input())
nums = [int(input()) for _ in range(N)]
set_nums = sorted(set(nums))
converted_index = {}
for i, num in enumerate(set_nums):
    converted_index[num] = i

# print(converted_index)

for num in nums:
    print(converted_index[num])
