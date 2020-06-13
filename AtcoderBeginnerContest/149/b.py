A, B, K = map(int, input().split())
if A < K:
    K = K - A
    A = 0
elif A == K:
    A = 0
    K = 0
else:  # K < A
    A = A - K
    K = 0

if B < K:
    K = K - B
    B = 0
elif B == K:
    B = 0
    K = 0
else:  # K < B
    B = B - K
    K = 0

print(A, B)
