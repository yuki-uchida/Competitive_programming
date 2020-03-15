import itertools
N = int(input())

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# max5この記号しか使えない.標準形は上から取っていけばいい


words = set([])
for i in range(1, N + 1):
    chars = alphabets[0:i]
    for j in range(1, i + 1):

        # texts = map(
        #     list, itertools.combinations_with_replacement(chars[:j], j))
        # for text in texts:
        #     words.add(''.join(text))
for word in sorted(list(words)):
    print(word)
