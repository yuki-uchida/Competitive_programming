A, B, C, K = map(int, input().split())


count = 0
if K - A >= 0:
    count += A
    K = K - A
    if K - B >= 0:
        count += 0
        K = K - B
        if K - C >= 0:
            count -= C
            print(count)
        else:
            count -= K
            print(count)
    else:
        count += 0
        print(count)
else:
    count += K
    print(count)
