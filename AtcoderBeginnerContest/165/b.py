X = int(input())

count = 0
num = 100
while num < X:
    num = int(num * 1.01)
    count += 1
print(count)
