N = int(input())
nums = list(map(int, input().split()))
LIS = [nums[0]]
ans = 0


def compute_total(start, count):
    if count % 2 == 0:
        return (start + 1) * (count // 2)
    else:
        return ((start + 1) * (count // 2)) + ((start + 1) // 2)


for i in range(1, N):
    # print(LIS)
    if LIS[-1] < nums[i]:
        LIS.append(nums[i])
    else:
        # print(len(LIS), compute_total(len(LIS), len(LIS)))
        ans += compute_total(len(LIS), len(LIS))
        # print(ans)
        LIS = [nums[i]]
# print(LIS)
ans += compute_total(len(LIS), len(LIS))

print(ans)
