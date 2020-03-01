N, M = list(map(int, input().split()))

pattern = []
for _ in range(N):
    pattern.append(None)


nums = []
for _ in range(M):
    nums.append(list(map(int, input().split())))


cant_bool = False

for keta, num in nums:
    if pattern[keta - 1] == None:
        pattern[keta - 1] = num
    else:
        if pattern[keta - 1] == num:
            continue
        else:
            cant_bool = True

if cant_bool and not (len(nums) == 0):
    print(-1)
else:
    if pattern[0] == 0 and len(pattern) > 1:
        print(-1)
    else:
        pattern = [(0 if (num == None) else num) for num in pattern]
        if pattern[0] == 0 and len(pattern) > 1:
            pattern[0] = 1
        print(''.join(map(str, pattern)))
