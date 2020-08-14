from collections import deque
N, K = map(int, input().split())
nums = list(map(str, input().split()))
can_use_nums = set([str(i) for i in range(10)])
for num in nums:
    can_use_nums.remove(num)
# print(can_use_nums)

queue = deque([[num] for num in can_use_nums if num != '0'])
# print(queue)
min_num = float('inf')
while queue:
    num = queue.popleft()
    if N <= int(''.join(num)):
        min_num = min(min_num, int(''.join(num)))
    else:
        for add_num in can_use_nums:
            t_num = num.copy()
            if min_num > int(''.join(num) + add_num):
                t_num.append(add_num)
                queue.append(t_num)
print(min_num)
