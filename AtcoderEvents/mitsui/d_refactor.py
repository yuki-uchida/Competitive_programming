N = int(input())
S = list(str(input()))

passwords = []
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            password = str(i) + str(j) + str(k)
            passwords.append(password)


for _ in range(3):
    password = ''
    for i in range(0, 10):
        password += str(i)


print(passwords)
char_hash = {}
for i, char in enumerate(S):
    if char in char_hash.keys():
        char_hash[char].append(i)
    else:
        char_hash[char] = [i]

print(char_hash)

# count = 0
# for password in passwords:
#     exist_keys = char_hash.keys()
#     # print(password[0] in char_hash.keys())
#     if not(password[0] in exist_keys):
#         continue
#     if not(password[1] in exist_keys):
#         continue
#     if not(password[2] in exist_keys):
#         continue
#     first_index = min(char_hash[password[0]])
#     second_indexes = char_hash[password[1]]
#     second_index = -1
#     for index in second_indexes:
#         if index <= first_index:
#             continue
#         else:
#             second_index = index
#             break
#     third_indexes = char_hash[password[2]]
#     third_index = -1
#     for index in third_indexes:
#         if index <= second_index:
#             continue
#         else:
#             third_index = index
#             break
#     # print(first_index, second_index, third_index)
#     if first_index < second_index and second_index < third_index:
#         count += 1

# print(count)
# print(len(passwords))
# print(passwords)
# print(set(passwords))
# print(len(list(set(passwords))))
