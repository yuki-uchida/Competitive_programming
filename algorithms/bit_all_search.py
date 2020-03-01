# money = 300
# item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
# n = len(item)
# for i in range(2 ** n):
#     bag = []
#     print("pattern {}: ".format(i), end="")
#     for j in range(n):  # このループが一番のポイント
#         if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
#             bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
#     print(bag)


n = 8
bags = []
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(bin(i)), end="")
    for j in range(n):  # アイテム分のループ
        if ((i >> j) & 1):  # 対象bitが1の時
            bag.append(1)  # フラグが立っていたら bag に果物を詰める
    bags.append(bag)
