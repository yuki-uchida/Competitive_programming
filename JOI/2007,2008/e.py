# 1<= R <= 10
# 1<= C <= 10000
import copy
R, C = list(map(int, input().split()))

crackers = []
for _ in range(R):
    crackers.append(list(map(int, input().split())))


return_bars_permutaion = []
for i in range(2**R):
    return_bars = []
    for j in range(R):
        if ((i >> j) & 1):
            return_bars.append(0)
        else:
            return_bars.append(1)
    return_bars_permutaion.append(return_bars)

sizes = []
for return_bars in return_bars_permutaion:
    return_crackers = []
    for i, bar in enumerate(return_bars):
        if bar:
            return_cracker = [
                0 if num else 1 for num in crackers[i]]
            return_crackers.append(return_cracker)
        else:
            return_crackers.append(crackers[i])
    size = 0
    for i in range(C):
        ura_count = 0
        for return_cracker_row in return_crackers:
            if return_cracker_row[i] == 0:
                ura_count += 1
            else:
                continue
        size += max(ura_count, R - ura_count)
    sizes.append(size)
# print(sizes)
print(max(sizes))
