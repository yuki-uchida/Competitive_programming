N = int(input())
points = list(map(int, input().split(" ")))

powers = []
for i in range(min(points), max(points) + 1):
    power = 0
    for point in points:
        power += ((i - point) ** 2)
    powers.append(power)

print(min(powers))
