N, K = map(int, input().split())
prices = sorted(map(int, input().split()))
print(sum(prices[0:K]))
