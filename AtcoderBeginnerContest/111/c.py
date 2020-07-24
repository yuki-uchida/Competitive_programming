from itertools import permutations
import collections
N = int(input())
nums = list(map(int, input().split()))
odd_nums = []
even_nums = []
for i, num in enumerate(nums):
    if i % 2 == 1:
        even_nums.append(num)
    else:
        odd_nums.append(num)

useable_nums = set(nums)
even_length = len(even_nums)
odd_length = len(odd_nums)
even_counter = collections.Counter(even_nums).most_common()
odd_counter = collections.Counter(odd_nums).most_common()
even_counter.append((0, 0))
odd_counter.append((0, 0))
even_counter.sort(key=lambda x: x[1], reverse=True)
odd_counter.sort(key=lambda x: x[1], reverse=True)
# print(even_counter)
# print(odd_counter)


min_ans = None
if even_counter[0][0] == odd_counter[0][0]:
    min_ans = min((odd_length - odd_counter[0][1]) + (even_length - even_counter[1][1]),
                  (odd_length - odd_counter[1][1]) + (even_length - even_counter[0][1]))
else:

    min_ans = odd_length - odd_counter[0][1] + even_length - even_counter[0][1]
print(min_ans)
