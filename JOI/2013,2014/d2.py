N = int(input())
hosts = list(input())
num_hosts = []
for host in hosts:
    if host == 'J':
        num_hosts.append(0)
    elif host == 'O':
        num_hosts.append(1)
    else:
        num_hosts.append(2)


dps = [[0 for _ in range(1 << 3)] for _ in range(N)]

for S in range(1 << 3):
    if (S & (1 << 0)) and (S & (1 << num_hosts[0])):
        dps[0][S] = 1
# print(dps)

for i in range(1, N):
    # print(i)
    for S in range(1 << 3):
        for prev_S in range(1 << 3):
            if prev_S & S == 0:
                continue
            if dps[i - 1][prev_S] == 0:
                continue
            if S & (1 << num_hosts[i]) == 0:
                continue
            # print(bin(prev_S), bin(S))
            dps[i][S] += dps[i - 1][prev_S]
# print(dps)
print(sum(dps[N - 1]) % 10007)
