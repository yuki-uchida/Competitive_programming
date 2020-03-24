N = int(input())

memos = [0 for _ in range(N + 1)]


def fibonacci(n, memos):
    memos[0] = 1
    memos[1] = 1
    for i in range(2, n + 1):
        memos[i] = memos[i - 1] + memos[i - 2]
    return memos[n]


print(fibonacci(N, memos))
