N = int(input())
schedules_hosts = list(input())
schedules_hosts_indexes = []
for host in schedules_hosts:
    if host == 'J':
        schedules_hosts_indexes.append(0)
    elif host == 'O':
        schedules_hosts_indexes.append(1)
    else:
        schedules_hosts_indexes.append(2)

# N日間のスケジュールを決める。
# 3人いて、それぞれが参加するしないの選択肢がある=8通り
# なので、8**N通りある

# 責任者を決め、その責任者は必ず出席する。残りの2人は参加するしないがある。よって4通り
# ただし、次の日の責任者は前日に出席して、鍵を持って帰らないといけない

# 考えられるスケジュールの数を算出する
# print(schedules_hosts_indexes)
dps = [[0 for _ in range(1 << 3)] for _ in range(N)]


for i in range(N - 1):
    for j in range(1 << 3):
        bin_j = '{:0=3}'.format(int(format(j, 'b')))
        if i == 0:
            if list(bin_j)[0] == '1' and list(bin_j)[schedules_hosts_indexes[i]] == '1':
                dps[i][j] = 1
                # print(bin_j)
                for k in range(1 << 3):
                    bin_k = '{:0=3}'.format(int(format(k, 'b')))
                    if list(bin_j)[schedules_hosts_indexes[i]] == '1' and list(bin_k)[schedules_hosts_indexes[i + 1]] == '1':
                        if '1' in '{:0=3}'.format(int(format(j & k, 'b'))):
                            # print(bin_j, bin_k)
                            dps[i + 1][k] += dps[i][j]
        else:
            if list(bin_j)[schedules_hosts_indexes[i]] == '1':
                for k in range(1 << 3):
                    bin_k = '{:0=3}'.format(int(format(k, 'b')))
                    if list(bin_j)[schedules_hosts_indexes[i]] == '1' and list(bin_k)[schedules_hosts_indexes[i + 1]] == '1':
                        if '1' in '{:0=3}'.format(int(format(j & k, 'b'))):
                            # print(bin_j, bin_k)
                            dps[i + 1][k] += dps[i][j]

print(sum(dps[N - 1]) % 10007)
