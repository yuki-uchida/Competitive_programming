from collections import deque
texts = deque(str(input()))
Q = int(input())


reverse = False
start_text = deque('')
end_text = deque('')
input_texts = []
for _ in range(Q):
    input_texts.append(list(input().split()))

for input_text in input_texts:
    if len(input_text) == 1:
        if reverse:
            reverse = False
        else:
            reverse = True
    else:
        if input_text[1] == '1':  # 先頭に
            if reverse:
                end_text.append(str(input_text[2]))
            else:
                start_text.appendleft(str(input_text[2]))
        else:  # 末尾に
            if reverse:
                start_text.appendleft(input_text[2])
            else:
                end_text.append(input_text[2])

# print(start_text, texts, end_text)
# print(''.join(texts))

texts.appendleft(''.join(start_text))
texts.append(''.join(end_text))
# print(''.join(texts))

# print(texts)
if reverse:
    texts = deque("".join(texts))
    texts.reverse()
    print("".join(texts))
else:
    # texts = start_text + texts + end_text
    print(''.join(texts))
