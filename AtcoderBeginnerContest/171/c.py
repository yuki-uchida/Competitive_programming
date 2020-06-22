N = int(input())
keta = 1
while True:
    if N > 26**keta:
        keta += 1
    else:
        break

# print(keta)
names = []
alphabets = 'abcdwfghijklmnopqrstuvwxyz'


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + '-' + str(X % n)
    return str(X % n)


# print(Base_10_to_n(N, 26))
# print(base10to(N, 26
for num in Base_10_to_n(N, 26).split("-"):
    names.append(alphabets[int(num) - 1])
print(''.join(names))
