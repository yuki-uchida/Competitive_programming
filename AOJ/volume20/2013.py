# 山手線は34.5Km
# 一周一時間かかる
# 駅は29駅ある
import itertools
while True:
    n = int(input())  # n <= 10000
    if n == 0:
        break
    timestamps = [0 for _ in range(24 * 60 * 60 + 1)]
    for _ in range(n):
        start, end = input().split()
        start_h, start_m, start_s = map(int, start.split(":"))
        start_h = start_h * 60 * 60
        start_m = start_m * 60
        start_time = start_h + start_m + start_s
        end_h, end_m, end_s = map(int, end.split(":"))
        end_h = end_h * 60 * 60
        end_m = end_m * 60
        end_time = end_h + end_m + end_s
        timestamps[start_time + 1] += 1
        timestamps[end_time + 1] -= 1
    timestamps = list(itertools.accumulate(timestamps))
    print(max(timestamps))
