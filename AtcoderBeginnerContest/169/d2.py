def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N = int(input())
ans = 0
# print(factorization(N))
for num, count in factorization(N):
    if num == 1:
        continue
    this_count = count
    start_x = 1
    while this_count - start_x >= 0:
        this_count -= start_x
        ans += 1
        start_x += 1
print(ans)
