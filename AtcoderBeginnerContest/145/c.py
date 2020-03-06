import itertools
import math
N = int(input())
cities = []
indexes = []
for i in range(N):
    cities.append(list(map(int, input().split())))
    indexes.append(i)


indexes_permutaions = list(itertools.permutations(indexes))
costs = []
for indexes_permutaion in indexes_permutaions:
    cost = 0
    for i in range(len(indexes_permutaion) - 1):
        index = indexes_permutaion[i]
        next_index = indexes_permutaion[i + 1]
        num = math.sqrt((((cities[next_index][0] - cities[index][0])
                          ** 2) + ((cities[next_index][1] - cities[index][1]) ** 2)))
        cost += num
    costs.append(cost)
print(float(sum(costs)) / len(costs))
