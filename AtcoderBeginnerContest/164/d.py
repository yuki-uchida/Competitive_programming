import sys
input = sys.stdin.readline
# 1<=S<=200000
S = str(input()).rstrip()
# print(len(S))
count = 0
for i in range(len(S) - 3):
    # print(i)
    # 0-4~8までやりたい
    for j in range(i + 4, i + 8):
        if j > len(S):
            continue
        print(i, j)
        if int(S[i:j]) % 2019 == 0:
            # print(i, j, S[i:j])
            count += 1
print(count)
