
nums = []
sum_nums = []
counts = []
while True:
    n, x = input().split(" ")
    n, x = int(n), int(x)
    if n == 0 and x == 0:
        break
    else:
        nums.append(n + 1)
        sum_nums.append(x)

for num, sum_num in zip(nums, sum_nums):
    count = 0
    for i in range(1, num):
        for j in range(i + 1, num):
            for k in range(j + 1, num):
                if (i + j + k) == sum_num:
                    count += 1
    counts.append(count)
for i, num in enumerate(counts):
    print(str(num))
