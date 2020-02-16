N = int(input())

existed_dict = {}
max_count = 0
max_text_list = []
for _ in range(N):
    text = input()
    if existed_dict.get(text):  # ここか
        existed_dict[text] += 1
    else:
        existed_dict[text] = 1
    if existed_dict[text] == max_count:
        max_count = existed_dict[text]
        max_text_list.append(text)
    elif existed_dict[text] > max_count:
        max_count = existed_dict[text]
        max_text_list = []
        max_text_list.append(text)
    else:
        pass

for text in sorted(max_text_list):  # ここ
    print(text)
