values = input().split(" ")

hash = {}
for value in values:
    hash[value] = 0

if len(hash.keys()) == 2:
    print("Yes")
else:
    print("No")
