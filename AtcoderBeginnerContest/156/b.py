n, k = list(map(int, input().split(" ")))


count = 1
num = k
while True:
    if n < num:
        break
    num = num * k
    count += 1
print(count)
