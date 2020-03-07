n, a, b = list(map(int, input().split(" ")))

blue_count = a * (n // (a + b))
n -= (a + b) * (n // (a + b))
if n >= a:
    blue_count += a
else:
    blue_count += n
print(blue_count)
