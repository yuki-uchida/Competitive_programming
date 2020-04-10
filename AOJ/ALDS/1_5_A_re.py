n = int(input())

nums = list(map(int, input().split()))
q = int(input())
target_nums = list(map(int, input().split()))
score_list = set()

for i in range(1 << n):
    ans = 0
    for j in range(n):
        if i >> j & 1:
            ans += nums[j]
    score_list.add(ans)
# print(score_list)
for num in target_nums:
    if num in score_list:
        print("yes")
    else:
        print("no")
