n = int(input())
A = []
for i in range(1, n + 1):
    c = int(input())
    if i % 2 == 1:
        if len(A) == 0:
            A.append([c, 1])
        elif A[-1][0] == c:
            A[-1][1] += 1
        else:
            A.append([c, 1])
    else:
        if A[-1][0] == c:
            A[-1][1] += 1
        else:
            b = A.pop()
            if len(A) == 0:
                A.append([c, b[1] + 1])
            else:
                A[-1][1] += b[1] + 1
cnt = 0
for j in range(len(A)):
    a = A[j]
    if a[0] == 0:
        cnt += a[1]
print(cnt)
