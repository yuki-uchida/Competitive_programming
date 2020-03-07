S = list(input())

a_count = 0
b_count = 0
for char in S:
    if char == 'A':
        a_count += 1
    else:
        b_count += 1

if ((a_count == 3) or (b_count == 3)):
    print("No")
else:
    print('Yes')
