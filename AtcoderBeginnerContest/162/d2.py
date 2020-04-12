N = int(input())
S = input()
r = 0
g = 0
b = 0
for i in range(N):
    if S[i] == "R":
        r += 1
    elif S[i] == "G":
        g += 1
    else:
        b += 1
ans = r * g * b

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        x = j + j - i
        if S[i] != S[j] and x <= N - 1:
            if S[i] != S[x] and S[x] != S[j]:
                ans -= 1

print(ans)
