S = list(input())
S = [char if char != '?' else None for char in S]
T = list(input())

# print(S)
# print(T)
# Tを部分文字列として含み、尚且つその中でもっとも辞書順で小さいものを選ぶ。
# 1<=S<=50なので、Sを全列挙することはできない(24**50)
# Sのうち、どこをTの部分文字列にするかを考えると、50文字あったとしても問題ないのでは？

texts = []
for i in range(len(S) + 1 - len(T)):
    # j = i + len(T)
    # print(S[i:j])

    is_fullfilled = True
    text = []
    for j, char in enumerate(T):
        if S[i + j] == char:
            text.append(char)
        elif S[i + j] is None:
            text.append(char)
        else:
            is_fullfilled = False
            break
    if is_fullfilled:

        text = ''.join(text)
        left = ''
        for char in S[:i]:
            if char is None:
                left += 'a'
            else:
                left += char
        right = ''
        for char in S[i + len(T):]:
            if char is None:
                right += 'a'
            else:
                right += char

        texts.append(left + text + right)
texts = sorted(texts)
if len(texts) == 0:
    print('UNRESTORABLE')
else:
    print(texts[0])
