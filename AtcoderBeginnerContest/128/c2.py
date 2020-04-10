N, M = map(int, input().split())
all_switches = [[] for _ in range(N)]

for i in range(M):
    input_text = list(map(int, input().split()))
    switches = input_text[1:]
    for switch in switches:
        all_switches[switch - 1].append(i)


# 電球が光る条件(M個)
lightup_terms = list(map(int, input().split()))
# print(all_switches)
count = 0
for i in range(1 << N):
    lightup_counts = [0 for _ in range(M)]
    for j in range(N):
        # 組み合わせを一つずつ確認する
        if i >> j & 1:
            for light in all_switches[j]:
                lightup_counts[light] += 1
    # print(lightup_counts)
    compute_success = True
    for j, term in enumerate(lightup_terms):
        if lightup_counts[j] % 2 != term:
            compute_success = False
            break
    if compute_success:
        count += 1
print(count)
