N = int(input())
count = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for _ in range(N):
    count[input()] += 1

print("AC x " + str(count["AC"]))
print("WA x " + str(count["WA"]))
print("TLE x " + str(count["TLE"]))
print("RE x " + str(count["RE"]))
