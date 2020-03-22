N = int(input())
balls = list(map(int, input().split()))
balls_count = {}
for ball_num in balls:
    if ball_num in balls_count.keys():
        balls_count[ball_num] += 1
    else:
        balls_count[ball_num] = 1
# print(balls_count)
indexes = {}
total_costs = []
count = 0
for k, v in balls_count.items():
    if count == 0:
        indexes[k] = count
        cost = int((v) * (v - 1) / 2)
        total_costs.append(cost)
        count += 1
    else:
        indexes[k] = count
        cost = (v) * (v - 1) / 2
        total_costs.append(int(total_costs[count - 1] + cost))
        count += 1
# print(indexes)
# print(total_costs)


for check_ball_num in balls:
    index = indexes[check_ball_num]
    if index == len(total_costs) - 1:
        if index - 1 >= 0:
            prev_cost = total_costs[index - 1]
            now_cost = (balls_count[check_ball_num] - 1) * \
                (balls_count[check_ball_num] - 2) / 2
            print(int(now_cost + prev_cost))
        else:
            now_cost = (balls_count[check_ball_num] - 1) * \
                (balls_count[check_ball_num] - 2) / 2
            print(int(now_cost))
    else:
        next_cost = (total_costs[index + 1] - total_costs[index])
        now_cost = (balls_count[check_ball_num] - 1) * \
            (balls_count[check_ball_num] - 2) / 2
        print(int(now_cost + next_cost))
