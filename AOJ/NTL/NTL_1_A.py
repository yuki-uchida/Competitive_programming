import math
input_num = int(input())
n = input_num
nums = []
# print(math.ceil(math.sqrt(n)))
for i in range(2, math.ceil(math.sqrt(n))):
    if n % i == 0:
        while n % i == 0:
            n = int(n / i)
            nums.append(str(i))
if n != 1:
    nums.append(str(n))


print(str(input_num) + ': ' + ' '.join(nums))
