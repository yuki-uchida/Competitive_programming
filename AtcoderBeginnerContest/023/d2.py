N = int(input())  # N <= 10^6
# H,S <= 10^10
baloons = [list(map(int, input().split())) for _ in range(N)]

max_heights = [baloon[0] + (baloon[1] * (N - 1)) for baloon in baloons]

left = min(max_heights)
right = max(max_heights)

while left <= right:
    mid = (left + right) // 2
    # 撃つ制限時間をだす
    limits = []
    can_make = True
    for height, speed in baloons:
        limit = (mid - height) // speed
        if limit < 0:
            can_make = False
            break
        else:
            limits.append(limit)
    limits = sorted(limits)
    for i in range(len(limits)):
        if limits[i] < i:
            can_make = False
            break
    if can_make:
        right = mid - 1
    else:
        left = mid + 1
print(left)
