K = int(input())
A, B = map(int, input().split())
if A <= K * (A // K) + K and K * (A // K) + K <= B:
    print("OK")
else:
    if A <= K * (A // K) and K * (A // K) <= B:
        print("OK")
    else:
        print("NG")
