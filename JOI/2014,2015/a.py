import itertools
N, M = map(int, input().split())
forward_use_rails_count = [0 for _ in range(N + 2)]
backward_use_rails_count = [0 for _ in range(N + 2)]
# これをまずは路線の被りを見つける。
# 1->2が120円,100円、30円だった時、路線の被りがn回だったら、どっちをとるか決める
# n*aと(n*b)+cで比較して安い方を使う
schedules = list(map(int, input().split()))
for i in range(1, M):
    if schedules[i] > schedules[i - 1]:
        left, right = schedules[i - 1], schedules[i]
        forward_use_rails_count[left] += 1
        forward_use_rails_count[right] -= 1
    else:
        left, right = schedules[i], schedules[i - 1]
        backward_use_rails_count[left] += 1
        backward_use_rails_count[right] -= 1
forward_use_rails_count = list(itertools.accumulate(forward_use_rails_count))
backward_use_rails_count = list(itertools.accumulate(backward_use_rails_count))
# print(forward_use_rails_count)
# print(backward_use_rails_count)
use_rails_count = [0 for _ in range(N + 2)]

for i in range(N + 2):
    use_rails_count[i] = forward_use_rails_count[i] + backward_use_rails_count[i]
# print(use_rails_count)


start_cost = 0
costs = []
for i in range(1, N):
    a, b, c = map(int, input().split())
    if use_rails_count[i] * a >= use_rails_count[i] * b + c:
        costs.append(b)
        start_cost += c
    else:
        costs.append(a)
costs = list(itertools.accumulate(costs))
costs.insert(0, 0)
# print(costs)

ans = 0
for i in range(1, M):
    if schedules[i] >= schedules[i - 1]:
        left, right = schedules[i - 1], schedules[i]
    else:
        left, right = schedules[i], schedules[i - 1]
    # print(costs[right - 1] - costs[left - 1])
    ans += costs[right - 1] - costs[left - 1]
# print(start_cost, ans)
ans += start_cost
print(ans)
