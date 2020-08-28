from itertools import accumulate

N, Q = map(int, input().split())
batches = [0 for _ in range(N + 1)]

for _ in range(Q):
    start, end = map(int, input().split())
    batches[start - 1] += 1
    batches[end] -= 1

batches = list(accumulate(batches))
batches = [str(num % 2) for num in batches[0:N]]
print("".join(batches))

