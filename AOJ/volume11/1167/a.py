inf = float('inf')


MAX = 10**6 + 1
dps = [inf for _ in range(MAX)]
dps[0] = 0
odddps = [inf for _ in range(MAX)]
odddps[0] = 0
print('a1')
for i in range(1, MAX):
    num = int(i * (i + 1) * (i + 2) / 6)
    for j in range(num, MAX):
        dps[j] = min(dps[j], dps[j - num] + 1)
        if num % 2 == 1:
            odddps[j] = min(odddps[j], odddps[j - num] + 1)
print('a')
while True:
    input_num = int(input())
    if input_num == 0:
        break
    print(dps[input_num], odddps[input_num])
