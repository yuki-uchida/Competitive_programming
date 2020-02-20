N = int(input()) + 1
nums_count = 0
for i in range(1, N):
    if i % 2 == 0:
        continue
    count = 1
    for j in range(1, int(i / 3) + 1):  # 8なら1,2,4,8で、1~4までやれば良い。最後に自分をたす あれ、もしかしてN/3?
        if i % j == 0:
            count += 1
    if count == 8:
        nums_count += 1

print(nums_count)
