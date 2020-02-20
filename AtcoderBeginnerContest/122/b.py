text = list(input())
atcoder_char = ['A', 'C', 'G', 'T']
for i, char in enumerate(text):
    if char not in atcoder_char:
        text[i] = ''

max_count = 0
count = 0
for char in text:
    if char in atcoder_char:
        count += 1
    else:
        if max_count < count:
            max_count = count
            count = 0

print(max_count) if max_count >= count else print(count)
