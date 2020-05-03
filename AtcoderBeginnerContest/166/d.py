X = int(input())

# Aの数は10**4個ある
# そして二分探索する

nums = [0]
n = 0
while (((n + 1)**5) - (n**5)) <= 10 ** 10:
    nums.append((n + 1)**5)
    n += 1
# print(nums)
ans = None
for num_a in nums:
    for num_b in nums:
        if num_a - num_b == X:
            ans = (num_a, num_b)
            break
        elif num_a + num_b == X:
            ans = (num_a, -1 * num_b)
            break
        elif (-1 * num_a) + num_b == X:
            ans = (-1 * num_a, num_b)
            break
        elif (-1 * num_a) - num_b == X:
            ans = (-1 * num_a, -1 * num_b)
            break
print(*ans)
