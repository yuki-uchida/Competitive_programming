from collections import deque
N = int(input())


queue = deque(['3', '5', '7'])

ans = set([])
while queue:
    now_nums = queue.popleft()
    if now_nums in ans or int(now_nums) > N:
        continue
    if len(now_nums) >= 3 and '3' in now_nums and '5' in now_nums and '7' in now_nums:
        ans.add(now_nums)
    for next_num in ['3', '5', '7']:
        if int(now_nums + next_num) > N:
            continue
        queue.append(now_nums + next_num)
print(len(ans))
