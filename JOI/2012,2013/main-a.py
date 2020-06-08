N = int(input())
lights = list(map(int, input().split()))
section = []
l = 0
while l < N:
    section.append(1)
    if l == N - 1:
        break
    for i in range(l, N - 1):
        if lights[i] != lights[i + 1]:
            section[-1] += 1
        else:
            l = i + 1
            break
    else:
        break
# print(section)
M = len(section)
if M == 1:
    print(section[0])
elif M == 2:
    print(sum(section))
else:
    ans = 0
    for i in range(1, M - 1):
        ans = max(ans, section[i - 1] + section[i] + section[i + 1])
    print(ans)
