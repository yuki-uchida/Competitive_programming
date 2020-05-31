N = int(input())
nums = sorted(map(int, input().split()))
if nums[0] == 0:
    print(0)
else:
    ans = 1
    for num in nums:
        ans = ans * num
        if ans > 10**18:
            break
    if ans > 10**18:
        print('-1')
    else:
        print(ans)
