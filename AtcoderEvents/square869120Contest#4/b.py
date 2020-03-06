# 1<=N<=K<=15
import itertools
N, K = list(map(int, input().split()))
buildings = list(map(int, input().split()))
indexes = [i for i in range(len(buildings))]
building_combinations = [
    combination for combination in itertools.combinations(indexes, K)]

costs = []
for building_combination in building_combinations:
    max_height = 0
    cost = 0
    for i, building in enumerate(buildings):
        if i in building_combination:  # 選んだ建物の場合
            if building <= max_height:
                cost += max_height - building + 1
                max_height = max_height + 1
            else:
                max_height = building
        else:
            if building >= max_height:
                max_height = building
    costs.append(cost)
# print(costs)
print(min(costs))
