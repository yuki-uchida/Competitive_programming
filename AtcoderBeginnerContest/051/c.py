sx, sy, tx, ty = map(int, input().split())
top = ty - sy
right = tx - sx
first = []

for _ in range(top):
    first.append('U')
for _ in range(right):
    first.append('R')


second = []
for char in first:
    if char == 'R':
        second.append('L')
    elif char == 'U':
        second.append('D')


third = ['L']
for _ in range(top + 1):
    third.append('U')
for _ in range(right + 1):
    third.append('R')
third.append('D')

forth = []
for char in third:
    if char == 'R':
        forth.append('L')
    elif char == 'U':
        forth.append('D')
    elif char == 'L':
        forth.append('R')
forth.append('U')
# print(first)
# print(second)
# print(third)
# print(forth)


print(''.join(first) + ''.join(second) + ''.join(third) + ''.join(forth))
