import itertools
N, M = list(map(int, input().split(" ")))

switches = []
for _ in range(M):
    l = list(map(int, input().split(" ")))
    switches.append(l[1:])


points = list(map(int, input().split(" ")))
# スイッチの数はN個。このkonおスイッチにon/offの状態があるので2^N
# これの全部の組み合わせを出して、条件を全て満たせる組み合わせがあればクリア
count = 0

# iは2n
for i in range(2**N):
    for j, switch in enumerate(switches):
        n = 0
        for k in switch:
            # print(i, k, i >> (k - 1))
            n += i >> (k - 1) & 1  # 該当bitが0or1が返す。なるほど。

        # print("========")
        if n % 2 == points[j]:
            continue
        else:
            break
    # breakによって抜けなかった時
    else:
        count += 1
print(count)
