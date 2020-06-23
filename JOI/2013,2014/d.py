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
# h:組み合わせのbit w: day
# 重要なことは、i日目に出席する人が決まれば、i+1日目に参加する人を決めるときに、i-1日目より以前のことを全く考えなくて良いところ。

# dps[i][S]は、i日目に、AOJの部分集合Sが出現する場合の数。ただし、ホストが参加していることが条件
dps = [[0 for _ in range(1 << 3)] for _ in range(N)]
MOD = 10007
for S in range(1 << 3):
    # TODO修正&右辺の意味を理解する
    if ((S & (1 << num_hosts[0])) != 0) and S & (1 << 0) != 0:
        dps[0][S] += 1

for i in range(1, N):
    for S in range(1, 1 << 3):
        # TODO修正
        if S & (1 << num_hosts[i]):
            T = set()
            for s in range(3):
                if S & (1 << s) == 0:
                    continue
                for A in range(1 << 3):
                    T.add((1 << s) | A)
            for t in T:
                dps[i][S] += dps[i - 1][t]
                dps[i][S] %= MOD
        else:
            dps[i][S] = 0

print(sum(dps[N - 1]) % MOD)
