
points = []
for _ in range(3):
    points.append(list(map(int, input().split())))

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))


for num in nums:
    for i in range(3):
        if num in points[i]:
            j = points[i].index(num)
            points[i][j] = 0

if (points[0][0] == 0) and (points[1][0] == 0) and (points[2][0] == 0):
    print("Yes")
elif (points[0][1] == 0) and (points[1][1] == 0) and (points[2][1] == 0):
    print("Yes")
elif (points[0][2] == 0) and (points[1][2] == 0) and (points[2][2] == 0):
    print("Yes")
elif (points[0][0] == 0) and (points[0][1] == 0) and (points[0][2] == 0):
    print("Yes")
elif (points[1][0] == 0) and (points[1][1] == 0) and (points[1][2] == 0):
    print("Yes")
elif (points[2][0] == 0) and (points[2][1] == 0) and (points[2][2] == 0):
    print("Yes")
elif (points[0][0] == 0) and (points[1][1] == 0) and (points[2][2] == 0):
    print("Yes")
elif (points[0][2] == 0) and (points[1][1] == 0) and (points[2][0] == 0):
    print("Yes")
else:
    print("No")
