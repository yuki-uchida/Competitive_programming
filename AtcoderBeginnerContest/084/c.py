N = int(input())
trains = []
for _ in range(N - 1):
    cost, start, f = map(int, input().split())
    trains.append([cost, start, f])

# print(trains)
for station_index in range(N - 1):
    ans = 0
    for j in range(station_index, N - 1):
        cost, start, f = trains[j]
        if ans < start:
            ans = start + cost
        elif ans == start:
            ans += cost
        else:
            if (ans - start) % f == 0:
                ans += cost
            else:
                ans += (f - (ans - start) % f) + cost
    print(ans)
print(0)
