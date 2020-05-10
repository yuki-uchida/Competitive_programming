S = list(str(input().rstrip()))
T = list(str(input().rstrip()))
# print(T[:len(S)])
if T[:len(S)] == S:
    print('Yes')
else:
    print('No')
