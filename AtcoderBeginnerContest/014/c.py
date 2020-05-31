import itertools
n = int(input())
requests = [0 for _ in range(10**6 + 2)]
for _ in range(n):
    start, end = map(int, input().split())
    requests[start] += 1
    requests[end + 1] -= 1
# print(requests[:100])
requests = list(itertools.accumulate(requests))
# print(requests[:100])
print(max(requests))
